# -*- coding: utf-8 -*-
#

import os, sys
import numpy as np

class compute:

    def __init__(self, dynamic_text, numeric_list):
        self.dynamic_text = dynamic_text
        self.static_text = "Hello from Python"
        self.numeric_list = numeric_list

    def get_static_text(self):
        return self.static_text

    def get_dynamic_text(self):
        return self.dynamic_text

    def add_to_list(self, added_values):
        self.numeric_list = self.numeric_list + added_values


    def get_mean(self):
    	if self.numeric_list.count > 0:
    		return np.mean(self.numeric_list)
    	else:
    		return -1

    def get_median(self):
    	if self.numeric_list.count > 0:
    		return np.median(self.numeric_list)
    	else:
    		return -1

    def get_min(self):
    	if self.numeric_list.count > 0:
    		return np.amin(self.numeric_list)
    	else:
    		return -1

    def get_max(self):
    	if self.numeric_list.count > 0:
    		return np.amax(self.numeric_list)
    	else:
    		return -1

    def get_standard_deviation(self):
    	if self.numeric_list.count > 0:
    		return np.std(self.numeric_list)
    	else:
    		return -1

    def get_square_root(self):
    	if self.numeric_list.count > 0:
    		return np.sqrt(self.numeric_list)
    	else:
    		return [-1]
