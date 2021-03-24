# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 02:56:45 2021

@author: danyu
"""

from odt_analysis import Odt_File_Tools

FILENAMES = ["./NZAFOFMRTests/NZAFO4000OeOPFMR.txt"]


def main():
    hyst = Odt_File_Tools()
    hyst.data_file = makefile(hyst)
    
    # Pull 
    
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
    
   
    
    
def makefile(test):    
    test.file_name = FILENAMES[0]
    test.extract()
    return test.data_file
    
    
    
    
if __name__ == '__main__':
    main()



