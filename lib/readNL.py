# -*- coding: utf-8 -*-


from pandas import Series, DataFrame
import pandas as pd
import csv

import re


def IONparser (ionCSVname): 


    print ('Start read ion settings file:',ionCSVname)
         
    # #---------------------------Open file----------------------#
  
    NLRaw = open (ionCSVname, 'r')
    
    
    print ('NL read END')
    return (prTYPElist,sumFrame)
