import configparser

class Get_Config:
    def __init__(self):
        self.config_parser = 'null'

    def initializeConfig(self):
        try:
            self.config_parser = configparser.ConfigParser()
            return self.config_parser
        except Exception as e:
            print ("Exception occured in Get_Config: " + str(e))
