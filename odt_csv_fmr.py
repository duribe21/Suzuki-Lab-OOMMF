#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:11:25 2021

@author: danyuribe
"""
import os, sys
from odt_analysis_v2 import ODT_File_Tools


def main(file, path):
    test = ODT_File_Tools()
    test.dir_path = path
    test.extract_data(file)

    
if __name__ == '__main__':
    file = str(sys.argv[1])
    path = str(sys.argv[2])
    main(file, path)