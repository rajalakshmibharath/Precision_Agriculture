import os
import urllib.request as request
import zipfile
from precision_agri import logger
from precision_agri.utils.common import get_size
from pathlib import Path

from precision_agri.constants import *
from precision_agri.utils.common import read_yaml, create_directories
from precision_agri.entity.config_entity import DataIngestionConfig


class DataIngestion:
		#we get the config from the Dataingestionconfig
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    #we download the file inside the 
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
