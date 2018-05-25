# -*- coding: utf-8 -*-
"""
Relief Header Calculation Program
"""

import math

# add abstract base class to hold pipe and frict factor tables?

class Header:
    def __init__(self, pipe_id, header_in_pressure, header_out_pressure, 
                 frict_factor, capacity):
        self.pipe_id = pipe_id # d
        self.header_in_pressure = header_in_pressure # p0
        self.header_out_pressure = header_out_pressure # p2
        self.frict_factor = frict_factor # f
        self.capacity = capacity # Cr
     
    def allow_length(self):
        d = self.pipe_id
        p0 = self.header_in_pressure
        p2 = self.header_out_pressure
        f = self.frict_factor
        Cr = self.capacity
        
        L = ((0.2146 * d**5 * ((p0**2)-(p2**2))) / (f * Cr**2)) \
        - (d * math.log(p0/p2, math.e))/(6 * f)
        return L
    
header1 = Header(0.824, 59.7, 20.8, 0.024, 20.2)
print(header1.allow_length())

# the math works!!