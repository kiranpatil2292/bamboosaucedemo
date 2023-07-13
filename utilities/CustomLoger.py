import logging
import os


class LogGen():
    @staticmethod
    def loggen():

        logger = logging.getLogger()
        file = logging.FileHandler(os.path.abspath(os.curdir) + "\\logs\\automation.log")
        Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        file.setFormatter(Format)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger
