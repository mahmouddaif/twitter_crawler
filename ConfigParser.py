#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

class ConfigsLoader:
    def __init__(self, configFileName):
        self.config = configparser.RawConfigParser()
        self.config.read(configFileName)
        
    def test(self):
        print(self.config)
        print(self.config.sections())
    
    def get_configs(self):
        return self.config        
        
    
def test_configsLoader():
    configFileName = "Configs.ini"
    configLoader = ConfigsLoader(configFileName)
    
    configLoader.test()
    
if __name__ == "__main__":
    test_configsLoader()
