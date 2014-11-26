# -*- coding: utf-8 -*-
#Copyright 2014 Zhixu Ni, AG Bioanalytik,BBZ,University of Leipzig            #
#The software is currently  under development and is not ready to be released.#
#A suitable license will be choosen before the offical release of mgfHunter.  #
#For more info please contact: zhixu.ni@uni-leipzig.de                        #

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
