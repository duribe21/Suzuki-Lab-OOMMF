#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:12:14 2021

@author: danyuribe
"""

import numpy as np
import os, sys
import pandas as pd
import scipy
from scipy.fftpack import rfftfreq, rfft
from scipy.signal import find_peaks

class ODT_File_Tools:
    def __init__(self):
        self.file_names = []
        self.dir_path = None
        self.data = None
        
    def extract_filenames(self):
        extension = ".csv"
        for roots, dirs, files in os.walk(self.dir_path):
            for file in files:
                if file.endswith(extension):
                    self.file_names.append(str(file))
                
        
    def extract_data(self, unique_key):
        self.extract_filenames()
        for test_file in self.file_names:
            if unique_key.lower() in test_file.lower():
                file_path = os.path.join(self.dir_path, test_file)
                self.data = pd.read_csv(file_path)
                self.data = self.data.rename(columns=lambda x: x.strip())
                
                self.fmr_columns()
                
                self.data.to_csv(os.path.join(self.dir_path, "FT_" + unique_key + ".csv"), index=False, )
                break
            
            
    def fmr_columns(self):
        length = self.data.shape[0]
        spacing = self.data["Oxs_TimeDriver::Simulation time (s)"][1] - self.data["Oxs_TimeDriver::Simulation time (s)"][0]
        self.data["FT Frequencies (Hz)"] = rfftfreq(length, spacing)
        
        mx = self.data["Oxs_TimeDriver::mx"]
        array_mx = np.array(mx)
        self.data["FT mx"] = np.abs(rfft(array_mx))
        
        my = self.data["Oxs_TimeDriver::my"].to_numpy()
        self.data["FT my"] = np.abs(rfft(my))
        
        mz = self.data["Oxs_TimeDriver::mz"].to_numpy()
        self.data["FT mz"] = np.abs(rfft(mz))
        
        
                
                