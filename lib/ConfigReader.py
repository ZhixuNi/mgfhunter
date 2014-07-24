from ConfigParser import ConfigParser

#import csv
#import numpy as np
#import os
#import string
#import pymzml

def getConfig (ConfigName,ParaSec): 
    # # Fetch parameters from the config file#
    CONFIGFILE = ConfigName
    SECTION =ParaSec
    config = ConfigParser()
    config.read(CONFIGFILE)
    
    # # Read detailed parameters from the config file#
    prTH_MS2 = config.getfloat(SECTION,'THMS2')
    prMS2_Low = config.getfloat(SECTION,'MS2TLLow')
    prMS2_High = config.getfloat(SECTION,'MS2TLHigh')
    prScore1 = config.getfloat(SECTION,'score1')
    prScore2 = config.getfloat(SECTION,'score2')

    
    # # return config info in a tuple#
    return (prTH_MS2,prMS2_Low,prMS2_High,prScore1,prScore2)
    
    
    #print ('WL2',DBEwl0O[2])