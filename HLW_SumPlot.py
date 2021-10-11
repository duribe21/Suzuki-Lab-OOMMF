#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 00:47:47 2021

@author: danyuribe
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FILE_NAMES = []
TITLE = "H_LW Summary Before and After Anneal"
XLABEL = "f (GHZ)"
YLABEL = "HWHM Linewidth (Oe)"

def DataFinder(path, extension):
    extensions = [".dat", ".txt", ".csv"]
    
    if not extension in extensions:
        print("Cannot reada data from this file type.\n")
    else:
        for root, dirs, files in os.walk(path):
            for filename in files:
                filename = str(filename)
                if filename.endswith(extension):
                    if "HLW" in filename:
                        FILE_NAMES.append(filename) 

def main():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    DataFinder(dir_path, ".dat")
    
    
    fill_value = 0
    conv= {i: lambda s: float(s.strip() or fill_value) for i in range(3)}
    
    for file in FILE_NAMES:
        
        x, y, error = np.genfromtxt(file, dtype="f8", converters=conv, skip_header=1, unpack=True)
        m, b = np.polyfit(x, y, 1)
        
        file_label = ("Before: " + "{:.2f}".format(m) + "x + " + "{:.2f}".format(b)) if ("Before" in file) else ("After: " + "{:.2f}".format(m) + "x + " + "{:.2f}".format(b)) 
        file_color ="b" if ("Before" in file) else "orange"
        
        plt.errorbar(x, y, error, fmt='o', color=file_color, label=file_label, ecolor='gray', elinewidth=1, capsize=5)
        #plt.plot(x,y,'o',color=file_color, label=file_label)
        plt.plot(x, m*x + b, file_color)
      
    plt.title(TITLE)
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()