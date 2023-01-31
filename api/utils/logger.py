import logging
import inspect

class Logger():

    def __init__(self):
        self.formatter = "[%(asctime)s] [%(name)s/%(levelname)s] %(message)s"
        self.fileTriggerInfo = f'FILE: {inspect.stack()[1][1]} LINE: {inspect.stack()[1][2]}'

        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        

    def debug(self, message):
        self.__handler(logging.DEBUG, 'debug.log', message)

    def info(self, message):
        self.__handler(logging.INFO, 'info.log', message)

    def warning(self, message):
        self.__handler(logging.WARNING, 'warning.log', message)

    def error(self, message):
        self.__handler(logging.ERROR, 'error.log', message)

    def critical(self, message):
        self.__handler(logging.CRITICAL, 'critical.log', message)


    def __handler(self, type=logging.INFO, fileToStore='info.log', message=''):

        if type != logging.INFO:
            logging.disable(logging.INFO)
            
        logging.basicConfig(
                filename=f'logs/{fileToStore}', 
                level=type, 
                format=self.formatter,
                force=True
            )

        if type == logging.DEBUG:
            logging.debug(f'[{self.fileTriggerInfo}] - [{message}]')
        elif type == logging.ERROR:
            logging.error(f'[{self.fileTriggerInfo}] - [{message}]')
        elif type == logging.WARNING:
            logging.warning(f'[{self.fileTriggerInfo}] - [{message}]')
        elif type == logging.CRITICAL:
            logging.critical(f'[{self.fileTriggerInfo}] - [{message}]')
        else:
            logging.info(f'[{self.fileTriggerInfo}] - [{message}]')


        logging.FileHandler(f'logs/{fileToStore}').close()
