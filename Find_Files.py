import os, glob
import configparser
from Rename_Files import Rename_Files


class Find_Files:
    def __init__(self, file_name, config_parser):
        self.file_name = file_name
        print("for finding files")
        self.config_parser = config_parser
        self.config_parser.read('conf/salesforce_config.ini')

    def findFile(self):
        try:
            print("finding files")
            self.download_path = self.config_parser.get('download_path', 'path')
            os.chdir(self.download_path)
            self.list_of_files = glob.glob("report*.xls")
            self.latest_file = max(self.list_of_files, key=os.path.getctime)
            print(self.latest_file)
            self.renamefile = Rename_Files(self.file_name, self.latest_file, self.config_parser)
            self.renamefile.renamingFiles()
        except Exception as e:
            print ("Exception occured in Find_files: " + str(e))
