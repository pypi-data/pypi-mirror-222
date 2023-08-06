#! /usr/bin/env python

import os
import sys
import time
from datetime import date
import numpy as np
import logging
import csv
import random
import warnings
import torch
from torch.autograd import Variable
from torch.nn import DataParallel
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SequentialSampler
from tqdm import tqdm
from cellmaps_utils import constants
import cellmaps_image_embedding
from cellmaps_utils import logutils
from cellmaps_utils.provenance import ProvenanceUtil
from cellmaps_image_embedding.exceptions import CellMapsImageEmbeddingError
from cellmaps_image_embedding.dataset import *
from cellmaps_image_embedding.models import *

logger = logging.getLogger(__name__)

ABB_LABEL_INDEX = {
    "0": "Nucleoplasm",
    "1": "N. membrane",
    "2": "Nucleoli",
    "3": "N. fibrillar c.",
    "4": "N. speckles",
    "5": "N. bodies",
    "6": "ER",
    "7": "Golgi app.",
    "8": "Peroxisomes",
    "9": "Endosomes",
    "10": "Lysosomes",
    "11": "Int. fil.",
    "12": "Actin fil.",
    "13": "F. a. sites",
    "14": "Microtubules",
    "15": "M. ends",
    "16": "Cyt. bridge",
    "17": "Mitotic spindle",
    "18": "MTOC",
    "19": "Centrosome",
    "20": "Lipid droplets",
    "21": "PM",
    "22": "C. Junctions",
    "23": "Mitochondria",
    "24": "Aggresome",
    "25": "Cytosol",
    "26": "C. bodies",
    "27": "Rods & Rings"
}


class EmbeddingGenerator(object):
    """
    Base class for implementations that generate
    network embeddings
    """
    def __init__(self, dimensions=1024):
        """
        Constructor
        """
        self._dimensions = dimensions

    def get_dimensions(self):
        """
        Gets number of dimensions this embedding will generate

        :return: number of dimensions aka vector length
        :rtype: int
        """
        return self._dimensions

    def get_next_embedding(self):
        """
        Generator method for getting next embedding.
        Caller should implement with ``yield`` operator

        :raises: NotImplementedError: Subclasses should implement this
        :return: Embedding
        :rtype: list
        """
        raise NotImplementedError('Subclasses should implement')


class FakeEmbeddingGenerator(EmbeddingGenerator):
    """
    Fakes image embedding
    """
    def __init__(self, inputdir, dimensions=1024,
                 suffix='.jpg', img_emd_translator=None):
        """
        Constructor

        :param inputdir: Directory where images reside under
                         red, green, blue, and yellow directories
        :type inputdir: str
        :param dimensions: Desired size of output embedding
        :type dimensions: int
        :param suffix: Image suffix with starting ``.``
        :type suffix: str
        """
        super().__init__(dimensions=dimensions)
        self._inputdir = inputdir
        self._suffix = suffix
        if img_emd_translator is None:
            self._img_emd_translator = ImageEmbeddingFilterAndNameTranslator(image_downloaddir=inputdir, fold=1)
        warnings.warn(constants.IMAGE_EMBEDDING_FILE +
                      ' contains FAKE DATA!!!!\n'
                      'You have been warned\nHave a nice day\n')
        logger.error(constants.IMAGE_EMBEDDING_FILE +
                     ' contains FAKE DATA!!!! '
                     'You have been warned. Have a nice day')

    def _get_image_id_list(self):
        """
        Looks at red directory under image directory to
        get a list of image ids which are the file names
        in that directory with last ``_`` and everything to
        the right of it removed from the file name
        :return:
        """
        image_set = set()
        red_image_dir = os.path.join(self._inputdir, constants.RED)
        for entry in os.listdir(red_image_dir):
            if not entry.endswith(self._suffix):
                continue
            if not os.path.isfile(os.path.join(red_image_dir, entry)):
                continue
            # include the _ at the end cause that is also included in
            # image_gene_node_attributes.tsv file
            image_set.add(entry[: entry.rfind('_')+1])
        return list(image_set)

    def get_next_embedding(self):
        """
        Generator method for getting next embedding.
        Caller should implement with ``yield`` operator

        :raises: NotImplementedError: Subclasses should implement this
        :return: Embedding
        :rtype: list
        """
        for image_id in self._get_image_id_list():
            if image_id not in self._img_emd_translator.get_name_mapping():
                continue
            g =  self._img_emd_translator.get_name_mapping()[image_id]

            row = [g]
            row.extend(np.random.normal(size=self.get_dimensions()))  # sample normal distribution
            prob = [g]
            prob.extend([random.random() for x in range(0, len(ABB_LABEL_INDEX.keys()))])  # might need to add to one
            yield row, prob


class DensenetEmbeddingGenerator(EmbeddingGenerator):
    """
    Runs densenet bundled with this tool via command line to
    generate embedding. Why do it this way? Easier transition
    from the original
    `Densenet <https://github.com/CellProfiling/densenet>`__
    code and no memory leaks

    """
    def __init__(self, inputdir, dimensions=1024,
                 outdir=None,
                 model_path=None,
                 suffix='.jpg',
                 fold = 1,
                 img_emd_translator=None):
        """
        Constructor

        :param inputdir: Directory where red, blue, green, and yellow
                         image directories reside
        :type inputdir: str
        :param dimensions: Desired size of output embedding vector
        :type dimensions: int
        :param pythonbinary: Path to python binary, if set to ``None``
                             the version of python that invoked this
                             command will be used
        :type pythonbinary: str
        :param predict: Path to prediction script. Default value is the
                        script bundled with this tool
        :type predict: str
        :param model_path: Path to model file
        :type model_path: str
        :param suffix: Image suffix with starting ``.``
        :type suffix: str
        :param img_emd_translator:
        """
        super().__init__(dimensions=dimensions)
        self._outdir = outdir
        self._inputdir = inputdir
        self.fold = fold
        self._gpus = ''
        self._image_size = 1536
        self._crop_size = 1024
        self._device = 'cpu'
        self._cuda_available = False
        self._model_path = os.path.abspath(model_path)
        self._suffix = suffix
        self._channels = 4
        self._num_classes = 28
        self._seeds = [0]
        self._augments = ['default']
        self._model = self._initialize_model()
        self._dataset = self._initialize_dataset()
        self._dataloader = self._initialize_dataloader()
        if img_emd_translator is None:
            self._img_emd_translator = ImageEmbeddingFilterAndNameTranslator(image_downloaddir=inputdir,
                                                                             fold=fold)

    def _initialize_model(self):
        """

        """
        model = class_densenet121_large_dropout(num_classes=self._num_classes,
                                                in_channels=self._channels,
                                                pretrained=self._model_path)
        model = DataParallel(model)
        model.to(self._device)
        model = model.eval()
        return model

    def _initialize_dataset(self):
        """

        :return:
        """
        dataset = ProteinDataset(
            self._inputdir,
            self._outdir,
            image_size=self._image_size,
            crop_size=self._crop_size,
            in_channels=self._channels,
            suffix=self._suffix,
            alt_image_ids=None)
        return dataset

    def _initialize_dataloader(self):
        """

        :return:
        """
        dataloader = DataLoader(
            self._dataset,
            sampler=SequentialSampler(self._dataset),
            batch_size=1,
            drop_last=False,
            num_workers=0,
            pin_memory=False,
        )
        return dataloader

    def get_next_embedding(self):
        """
        Generator method for getting next embedding.

        :return: Embedding vector with 1st element
        :rtype: list
        """
        for seed in self._seeds:
            for augment in self._augments:
                np.random.seed(seed)
                torch.manual_seed(seed)
                # eg. augment_default
                transform = eval("augment_%s" % augment)
                self._dataloader.dataset.set_transform(transform=transform)
                random_crop = (self._crop_size > 0) and (seed != 0)
                self._dataloader.dataset.set_random_crop(random_crop=random_crop)
                image_ids = np.array(self._dataloader.dataset.image_ids)

                for iter_index, (images, indices) in tqdm(
                    enumerate(self._dataloader, 0), total=len(self._dataloader)
                ):
                    with torch.no_grad():
                        if self._cuda_available:
                            images = Variable(images.cuda())
                        else:
                            images = Variable(images)
                        logits, features = self._model(images)

                        image_id = image_ids[iter_index] + '_'
                        if image_id not in self._img_emd_translator.get_name_mapping():
                            continue
                        g =  self._img_emd_translator.get_name_mapping()[image_id]
                        # probabilities
                        probs = F.sigmoid(logits)
                        prob_list = [g]
                        prob_list.extend(probs.cpu().data.numpy().tolist()[0])

                        # features
                        features = features.cpu().data.numpy().tolist()
                        row = [g]
                        row.extend(features[0])
                        del features
                        del logits
                        yield row, prob_list



class ImageEmbeddingFilterAndNameTranslator(object):
    """
    Converts image embedding names and filters keeping only
    one per gene

    """

    def __init__(self, image_downloaddir=None, fold = 1):
        """
        Constructor
        """
        self._id_to_gene_mapping = self._gen_filtered_mapping(os.path.join(image_downloaddir, str(fold) + '_' +
                                                                           constants.IMAGE_GENE_NODE_ATTR_FILE))

    def _gen_filtered_mapping(self, image_gene_node_attrs_file):
        """
        Reads TSV file

        :param image_gene_node_attrs_file:
        :return:
        """
        mapping_dict = {}
        with open(image_gene_node_attrs_file, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                mapping_dict[row['filename'].split(',')[0]] = row['name']
        return mapping_dict

    def get_name_mapping(self):
        """
        Gets mapping of old name to new name

        :return: mapping of old name to new name
        :rtype: dict
        """
        return self._id_to_gene_mapping
                        
                        
class CellmapsImageEmbedder(object):
    """
    Class to run algorithm
    """
    def __init__(self, outdir=None,
                 inputdir=None,
                 embedding_generator=None,
                 name=None,
                 organization_name=None,
                 project_name=None,
                 input_data_dict=None,
                 provenance_utils=ProvenanceUtil()):
        """
        Constructor

        :param outdir: Directory to write the results of this tool
        :type outdir: str
        :param inputdir: Output directory from cellmaps_imagedownloader
        :type inputdir: str
        :param embedding_generator:
        :param name:
        :type name: str
        :param organization_name:
        :type organization_name: str
        :param project_name:
        :type project_name: str
        :param input_data_dict:
        :type input_data_dict: dict
        :param provenance_utils:

        """
        logger.debug('In constructor')
        if outdir is None:
            raise CellMapsImageEmbeddingError('outdir is None')
        self._outdir = os.path.abspath(outdir)
        self._inputdir = inputdir
        self._start_time = int(time.time())
        self._name = name
        self._project_name = project_name
        self._organization_name = organization_name
        self._provenance_utils = provenance_utils
        self._embedding_generator = embedding_generator
        self._softwareid = None
        self._input_data_dict = input_data_dict
        self._image_embedding = None
     
    def _create_rocrate(self):
        """
        Creates rocrate for output directory

        :raises CellMapsProvenanceError: If there is an error
        """
        name, proj_name, org_name = self._provenance_utils.get_name_project_org_of_rocrate(self._inputdir)

        if self._name is not None:
            name = self._name

        if self._organization_name is not None:
            org_name = self._organization_name

        if self._project_name is not None:
            proj_name = self._project_name
        try:
            self._provenance_utils.register_rocrate(self._outdir,
                                                    name=name,
                                                    organization_name=org_name,
                                                    project_name=proj_name)
        except TypeError as te:
            raise CellMapsImageEmbeddingError('Invalid provenance: ' + str(te))
        except KeyError as ke:
            raise CellMapsImageEmbeddingError('Key missing in provenance: ' + str(ke))

    def _create_output_directory(self):
        """
        Creates output directory if it does not already exist

        :raises CellmapsDownloaderError: If output directory is None or if directory already exists
        """
        if os.path.isdir(self._outdir):
            raise CellMapsImageEmbeddingError(self._outdir + ' already exists')

        os.makedirs(self._outdir, mode=0o755)
        for cur_color in constants.COLORS:
            cdir = os.path.join(self._outdir, cur_color + '_resize')
            if not os.path.isdir(cdir):
                logger.debug('Creating directory: ' + cdir)
                os.makedirs(cdir,
                            mode=0o755)

    def _register_software(self):
        """
        Registers this tool

        :raises CellMapsImageEmbeddingError: If fairscape call fails
        """
        self._softwareid = self._provenance_utils.register_software(self._outdir,
                                                                    name=cellmaps_image_embedding.__name__,
                                                                    description=cellmaps_image_embedding.__description__,
                                                                    author=cellmaps_image_embedding.__author__,
                                                                    version=cellmaps_image_embedding.__version__,
                                                                    file_format='.py',
                                                                    url=cellmaps_image_embedding.__repo_url__)

    def _register_computation(self):
        """
        Registers computation with FAIRSCAPE

        """
        logger.debug('Getting id of input rocrate')
        input_dataset_id = self._provenance_utils.get_id_of_rocrate(self._inputdir)

        self._provenance_utils.register_computation(self._outdir,
                                                    name=cellmaps_image_embedding.__name__ + ' computation',
                                                    run_by=str(self._provenance_utils.get_login()),
                                                    command=str(self._input_data_dict),
                                                    description='run of ' + cellmaps_image_embedding.__name__,
                                                    used_software=[self._softwareid],
                                                    used_dataset=[input_dataset_id],
                                                    generated=[self._image_embedding])

    def _register_image_embedding_file(self):
        """
        Registers image_gene_node_attributes.tsv file with create as a dataset

        """
        data_dict = {'name': cellmaps_image_embedding.__name__ + ' output file',
                     'description': 'Image gene node attributes file',
                     'data-format': 'tsv',
                     'author': cellmaps_image_embedding.__name__,
                     'version': cellmaps_image_embedding.__version__,
                     'date-published': date.today().strftime('%m-%d-%Y')}
        self._image_embedding = self._provenance_utils.register_dataset(self._outdir,
                                                                        source_file=self.get_image_embedding_file(),
                                                                        data_dict=data_dict,
                                                                        skip_copy=True)

    def get_image_embedding_file(self):
        """
        Gets image embedding file
        :return:
        """
        return os.path.join(self._outdir, constants.IMAGE_EMBEDDING_FILE)

    def get_image_probability_file(self):
        """
        Gets image probability file
        :return:
        """
        return os.path.join(self._outdir, "labels_prob.tsv")
    
    def get_name_mapping(self):
        """

        :return:
        """
        return self._img_emd_translator.get_oldname_to_new_name_mapping()
    
    def run(self):
        """
        Runs cellmaps_image_embedding


        :return:
        """
        exitcode = 99
        try:
            logger.debug('In run method')
            self._create_output_directory()

            logutils.setup_filelogger(outdir=self._outdir,
                                      handlerprefix='cellmaps_image_embedding')
            logutils.write_task_start_json(outdir=self._outdir,
                                           start_time=self._start_time,
                                           data={'imagedir': self._inputdir},
                                           version=cellmaps_image_embedding.__version__)

            if self._inputdir is None:
                raise CellMapsImageEmbeddingError('inputdir must be set')

            self._create_rocrate()

            self._register_software()

            # generate result
            raw_embeddings = []
            with open(self.get_image_embedding_file(), 'w', newline='') as f:
                with open(self.get_image_probability_file(), 'w', newline='') as pf:
                    writer = csv.writer(f, delimiter='\t')
                    prob_writer = csv.writer(pf, delimiter='\t')
                    header_line = ['']
                    header_line.extend([x for x in range(1, self._embedding_generator.get_dimensions())])
                    writer.writerow(header_line)
                    header_line_prob = ['']
                    for key in range(0,len(ABB_LABEL_INDEX.keys())):
                        header_line_prob.append(ABB_LABEL_INDEX[str(key)])
                    prob_writer.writerow(header_line_prob)
                    for row, prob_list in self._embedding_generator.get_next_embedding():
                        writer.writerow(row)
                        raw_embeddings.append(row)
                        prob_writer.writerow(prob_list)
 
            self._register_image_embedding_file()

            self._register_computation()
            exitcode = 0
        finally:
            logutils.write_task_finish_json(outdir=self._outdir,
                                            start_time=self._start_time,
                                            status=exitcode)

        return exitcode

