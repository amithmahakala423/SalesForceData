from selenium import webdriver
import time
from Get_Config import Get_Config
from Rename_Files import Rename_Files
from Find_Files import Find_Files


class Report_Data:
    def __init__(self, driver):
        #initializing webdriver for chrome
        self.driver = driver;
        self.get_config = Get_Config()
        #getting the config_parser reference
        self.config_parser = self.get_config.initializeConfig()
        self.config_parser.read('conf/salesforce_config.ini')


    def dataDownload(self):
        try:
            self.urlNumber = 1
            self.urlPre = 'url_'
            self.namePre = 'name_'
            self.urlSuff = self.urlPre + str(self.urlNumber)
            self.nameSuff = self.namePre + str(self.urlNumber)
            print (self.urlSuff)
            while str(self.config_parser.get('salesforce_urls', self.urlSuff)) != '':
                self.driver.get(str(self.config_parser.get('salesforce_urls', self.urlSuff)))
                print("Opening page......")
                time.sleep(2);
                self.button = self.driver.find_element_by_name('csvsetup')
                self.button.click()
                print ("Clicked Export Details Button")
                time.sleep(2)
                self.button = self.driver.find_element_by_name('export')
                self.button.click()
                print("Clicked Export Button..file ready to download")
                time.sleep(5)
                self.findfile = Find_Files(str(self.config_parser.get('file_names', self.nameSuff)), self.config_parser)
                self.findfile.findFile()
                self.urlNumber += 1
                self.urlSuff = self.urlPre + str(self.urlNumber)
                self.nameSuff = self.namePre + str(self.urlNumber)
                print (self.urlSuff)
        except Exception as e:
            print ("Exception occured in Report_Data" + str(e))


    def findRenameFiles(self):
        self.findfiles = Find_Files()
        self.findfiles.findFiles()

sfdata = Report_Data(webdriver.Chrome())
sfdata.dataDownload()
