#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

def mkdir(path_):
    if not os.path.exists(path_):
        os.makedirs(path_)
        print("Directory " , path_ ,  " Created ")
    else:    
        print("Directory " , path_ ,  " already exists")    

def write_list_to_file(my_list, file_name):
    file = open(file_name, "a")
    file.write(','.join(my_list)+"\n")
        
    file.close()
    
    
def create_file(file_name):
    file = open(file_name, "w")
    file.close()
    
    
def file_exists(file_name):
    return os.path.isfile(file_name) 

def read_words_list(file_name):
    with open(file_name) as f: 
        lines = f.read().splitlines()
        
    lines = [line.strip() for line in lines]
    lines = list(set(lines))
    print("Number of track terms is: ", len(lines))
    return lines

if __name__ == "__main__": 
    (read_words_list("words_list.txt"))
