import configparser

class Get_Config:
    def __init__(self):
        self.config_parser = 'null'

    def initializeConfig(self):
        self.config_parser = configparser.ConfigParser()
        return self.config_parser
