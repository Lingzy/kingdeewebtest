import os
import logging
import time
from logging.handlers import TimedRotatingFileHandler
from .config import LOG_PATH,Config



class Logger(object):
    def __init__(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log')
        self.log_file_name = time.strftime('%Y-%m-%d') + '.log'
        self.backup_count = c.get('backup') if c and c.get('backup') else 5
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        if not self.logger.handlers:
            console_hander = logging.StreamHandler()
            console_hander.setFormatter(self.formatter)
            console_hander.setLevel(self.console_output_level)
            self.logger.addHandler(console_hander)

            file_hander = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                   when='D',interval=1,backupCount=self.backup_count,
                                                   delay=True,encoding='utf-8')
            file_hander.setFormatter(self.formatter)
            file_hander.setLevel(self.file_output_level)
            self.logger.addHandler(file_hander)
        return self.logger


logger = Logger().get_logger()

