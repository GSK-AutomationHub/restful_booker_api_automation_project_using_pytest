import logging
from src.utils.prop_reader import PropReader

class LogsGenerator:

    @staticmethod
    def get_logger():
        logging.basicConfig(filename=PropReader.read_config_file("logfile_info", "logfile_name"),
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',force=True)
        return logging.getLogger()