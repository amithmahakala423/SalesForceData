import configparser
import os


class Rename_Files:
    def __init__(self, file_name, latest_file, config_parser):
        print(" for renaming files")
        self.file_name = file_name
        self.latest_file= latest_file
        self.config_parser = config_parser
        self.config_parser.read('conf/salesforce_config.ini')

    def renamingFiles(self):
        print ('renaming files')
        self.download_path = self.config_parser.get('download_path', 'path')
        os.chdir(self.download_path)
        os.rename(self.latest_file, self.file_name)



