# -*- coding: utf-8 -*-
#Copyright 2014 Zhixu Ni, AG Bioanalytik,BBZ,University of Leipzig            #
#The software is currently  under development and is not ready to be released.#
#A suitable license will be choosen before the offical release of mgfHunter.  #
#For more info please contact: zhixu.ni@uni-leipzig.de                        #


from __future__ import division

def IONmass (MASS, MASStype, pepMASS=None, prCHG=None, ionCHG=None):
      
    ionMZ_list =[]     
    if ionCHG == None:
        ionCHG = 1
    else:
         pass      
    
    if isinstance(MASS,float) and isinstance(ionCHG,int):
        pass
    else:
        try:
            MASS = float (MASS)
            ionCHG = int (ionCHG)
        except:
            print 'Input ERROR !'
    
    H = 1.00783
        
    if MASStype == 'FRAG' or MASStype == 'F':
        
        #ionMZ = (MASS + ionCHG * H)/ionCHG
        ionMZ = MASS
        ionMZ_list = [(ionMZ,ionCHG)]
        
    if MASStype == 'NL' or MASStype == 'N':
        if prCHG == None:
            prCHG = 1
        else:
            pass
        if isinstance(pepMASS,float) and isinstance(prCHG,int):
            pass
        else:
            try:
                pepMASS = float (pepMASS)
                prCHG = int (prCHG)
            except:
                print 'Input ERROR !'

            
        orignalMASS = (pepMASS * prCHG) - prCHG * H
        ionCHG_List = range(1,prCHG+1)
        #print ionCHG_List
        for ionCHG in ionCHG_List:
            ionMZ = ((orignalMASS - MASS) + ionCHG * H)/ionCHG
            ionINFO = (ionMZ,ionCHG)
            ionMZ_list.append(ionINFO)
    
    return ionMZ_list
    
def PRmass (pepMASS, charge):
    
    if isinstance(pepMASS,float) and isinstance(charge,int):
        pass
        
    else:
        try:
            pepMASS = float (pepMASS)
            charge = int (charge)
        
        except:
            print 'Input ERROR !'
            
    H = 1.00783
    originMASS = (pepMASS * charge) - charge * H
    
    return originMASS