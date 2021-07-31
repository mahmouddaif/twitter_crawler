#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils import mkdir, write_list_to_file, create_file, file_exists

class CSVManager:
    def __init__(self, folder_name):
        
        mkdir(folder_name)
        
    def write_list_to_file(self, my_list, file_name):
        if file_exists(file_name): 
            write_list_to_file(my_list, file_name)
        else:
            create_file(file_name)
            write_list_to_file(my_list, file_name)