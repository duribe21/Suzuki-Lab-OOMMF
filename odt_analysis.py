# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 23:54:58 2021

@author: danyu
"""
import json

import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.fftpack import rfftfreq, rfft
from scipy.signal import find_peaks

class Odt_File_Tools:
    def __init__(self):
        self.file_name = None
        self.data_file = None
    
        
    
    
    def extract(self):
        if self.file_name == None:
            print("Specify .odt file path to variable file_name")
            return
        with open(self.file_name) as file:
            full = []
            for i in range(12):
                next(file)
            for line in file:
                line = line.strip()
                new = line.split()
                full.append(new)
            full.pop(-1)
            # Create json file name, can be renamed later with self.data_file
            output_file = self.file_name[-20:-4] + ".json"
            self.data_file = output_file
            with open(output_file, 'w') as outfile:
                json.dump(full, outfile, indent=2)
                
                
        
    def list_data(self, index = -1):
        if self.data_file == None:
            print("Specify .json path to variable data_file")
            return
        input_file = open(self.data_file)
        json_array = json.load(input_file)
        data = []
        # check if index is valid
        if abs(index) >= len(json_array[0]):
                print("Index is out of bounds. -1 for run time")
                return
        for line in json_array:
            data.append(line[index])
        data_array = np.array(data)
        return data_array
    
    

    def time_to_freq(self, time):
        """
        Fourier transform time passed to create frequencies
        :param time: Time passed in simulation
        :return: list of frequencies
        """
        N = len(time)
        T = float(time[1]) - float(time[0])
        freq = rfftfreq(N, T)
        freq = np.array(freq)
        return freq
    
    
        
    def ft_data(self, data):
        """
        Performs fourier transform on data, must be array
        """
        data_ft = rfft(data)
        data_ft = np.abs(data_ft)
        return data_ft
    
    

    def plot(self, x_data, y_data):
        """
        state = input("Specify plot details? Title, etc? True, False ")
        if state == True:
            title = input("Title? ")
            plt.title(title)
            xlabel = input("X axis title? ")
            plt.xlabel(xlabel)
            ylabel = input("Y axis title? ")
            plt.xlabel(ylabel)
        """
        plt.plot(x_data, y_data, color = 'b')
        plt.show()
        
        
        
    def peak_index(self, data, final_data = None, min_height = 1):
        peaks, _ = scipy.signal.find_peaks(data, prominence = min_height)
        comp_data = data
        # Account for fmr where freq is of concern, but peaks are from ft mx, my, mz
        if len(final_data) != 0:
            comp_data = final_data
        # pick out one major peak per every cluster
        max_points = []
        if len(peaks) != 0:
            selected_peaks = [peaks[0]]
            for j in range(1, len(peaks)):
                if (peaks[j] - selected_peaks[-1]) > 5:
                    selected_peaks.append(peaks[j])
                elif comp_data[peaks[j]] > comp_data[selected_peaks[-1]]:
                    selected_peaks[-1] = peaks[j]
            for peak in selected_peaks:
                max_points.append(comp_data[peak])
        # implicit else to account for case of no peaks
        return max_points
        
        
            

            
    
    
    
    