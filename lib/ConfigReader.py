# -*- coding: utf-8 -*-
#Copyright 2014 Zhixu Ni, AG Bioanalytik,BBZ,University of Leipzig            #
#The software is currently  under development and is not ready to be released.#
#A suitable license will be choosen before the offical release of mgfHunter.  #
#For more info please contact: zhixu.ni@uni-leipzig.de                        #

from ConfigParser import ConfigParser


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
    