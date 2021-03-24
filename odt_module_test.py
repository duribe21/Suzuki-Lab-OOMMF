# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 01:47:15 2021

@author: danyu
"""
import matplotlib.pyplot as plt
from odt_analysis import Odt_File_Tools

FILENAMES = ["./NZAFOFMRTests/NZAFO4000OeOPFMR.txt"]


def main():
    fmr = Odt_File_Tools()
    fmr.data_file = "NZAFO4000OeOPFMR.json"
    
    # Pull time data
    time = fmr.list_data()
    freq = fmr.time_to_freq(time)
    
    # Iterative analysis
    for dim in range(-5, -2):
        data = fmr.list_data(dim)
        ft_data = fmr.ft_data(data)
        
        """ 
        Major difference of FMR to other tests, must pass in freq along with 
        ft_data to 
        """
        peaks = fmr.peak_index(ft_data, freq, 0.5)
        print(peaks)
        
        plt.plot(freq, ft_data)
    
    plt.show()
    
   
    
    
def makefile(fmr):    
    fmr.file_name = FILENAMES[0]
    fmr.extract()
    return fmr.data_file
    
    
    
    
if __name__ == '__main__':
    main()

