# -*- coding: utf-8 -*-
from __future__ import division
from pyteomics import mgf
from lib.IONcalc import IONmass
from lib.IONcfg import CFGparser
from lib.ConfigReader import ConfigParser 
import pandas as pd
import re
import time
import winsound


def Hunter(inmgf,outmgf,cfgNAME=None,cfgSection=None,ionCSVname=None):
    stTIME = time.clock()


    inmgf = inmgf.encode("utf-8")
    outmgf = outmgf.encode("utf-8")
    config = ConfigParser()
    config.read(cfgNAME)

    SECTION = cfgSection
    
    PRrTH = config.get(SECTION,'THMS2')
    rTH = float(PRrTH) * 0.01
    rTH = float(rTH)
    
    delta_L = float(config.get(SECTION,'MS2TLLow'))
    delta_H = float(config.get(SECTION,'MS2TLHigh'))
    
    ScoreTH1 = float(config.get(SECTION,'score1'))
    ScoreTH2 = float(config.get(SECTION,'score2'))
    
    ionSet = CFGparser(ionCSVname)
    
    stinfo = [SECTION,rTH,ScoreTH1,ScoreTH2]
    
    print stinfo

    cfg_df_q = ionSet.CFGread()
    print cfg_df_q
    
    #absTH_List = []

    ##############Settings finished ################

    #print 'inmgf',inmgf
    #inmgf = inmgf.replace("/", "\\")
    #outmgf = outmgf.replace("/", "\\")
    #print 'raw string inpmgf:',inmgf
    
    
    with mgf.read(inmgf) as spectra:
        print "got file"
        
        for reader in spectra:
            #print "reading"
            # #reader['params'] is a dict# #
            tmp_header = reader['params']
            reader_info = {'params':reader['params'],
                            'm/z array': reader['m/z array'],
                            'intensity array': reader['intensity array']}
    
            pepinfo =  tmp_header['pepmass']
            #print pepinfo
            pepMZ = pepinfo[0]
            #pepI = pepinfo[1]
            try:
                CHGinfo =  tmp_header['charge']
                prCHG = CHGinfo[0]
            except KeyError:
                prCHG = 1
            RT = float(tmp_header['rtinseconds'])
    
            # calculation of peptide mass
            #pepMZcalc = PRmass(pepMZ, prCHG)
    
            x = tmp_header['title']
            y = x.strip(" \" ")
            ScanID = re.compile(r'=')
            ID = ScanID.split(y)
            ScanID = ID[-1]
            #ScanID = 'ScanID ' + str(ScanID)
    
            # get Max intensity #
            i_max = max(reader['intensity array'])
            
            LS_lenth = len(reader['m/z array'])
            ScanID_List = [ScanID]*LS_lenth
    
            tmp_spec = {'ScanID': ScanID_List,
                        'mz': reader['m/z array'],
                        'i': reader['intensity array']}
        
            
            tmpSpec_pd = pd.DataFrame(tmp_spec,columns=['ScanID','mz', 'i'])
            


            tmp_found_List =[]
            # # intensity filter# #
            absTH = float(rTH * i_max)
            #print absTH
            #absTH_List.append(absTH)

            
            tmpSpec_pd_TH = tmpSpec_pd[tmpSpec_pd['i'] >= absTH]
            #print tmpSpec_pd_TH, absTH
            #tmpSpec_pd_TH.tail(3)
            
            # # ion hunter # #

            totScore = 0
            for ion in cfg_df_q['ionName']:
                
                ion_df = cfg_df_q[cfg_df_q['ionName']==ion]
                
                MASS = ion_df.iloc[0]['ionMASS']
                MASStype = ion_df.iloc[0]['ionTYPE']
                ionCHG = ion_df.iloc[0]['ionCHG']
                ionScore = ion_df.iloc[0]['ionScore']
                RT1 = float(ion_df.iloc[0]['RT1'])
                RT2 = float(ion_df.iloc[0]['RT2'])
                #print RT, RT1, RT2
                
                #print 'RT in range'
                #if MASStype == 'F':
                #    ionMZ = float(MASS)
                #if MASStype == 'N':
                if RT1 <= RT <= RT2:
                    ionMZ = IONmass (MASS, MASStype, \
                                    pepMZ, prCHG, ionCHG)
                                
                    ion_L = ionMZ-delta_L
                    ion_H = ionMZ+delta_H
                    
        
                    temp_query = str(ion_L) + r'<= mz <=' + str(ion_H)
                    temp_query_info = tmpSpec_pd_TH.query(temp_query)
                    #print ScanID,'',temp_query_info
                    found_mz_list =temp_query_info.iloc[:]['mz'].tolist()
                    
                    
                
                    if len(found_mz_list) >0:
                        #temp_ion_pd = temp_ion_pd.append(temp_query_info)
                        tmp_ion_info = [ion,MASS,found_mz_list]
                        tmp_found_List.append(tmp_ion_info)
                        totScore = totScore + ionScore
                        #print tmp_ion_info
                    else:
                        #print 'ion',ion,'not found!'
                        pass
                
            if ScoreTH1<= float(totScore) <=ScoreTH2:
                mgf.write(reader_info, output= outmgf,header='') 
                print '#',ScanID, '=GET Score==>',totScore 
            else:
                #print 'No Frag/NL found',ScanID
                pass

                    
    
    print 'finished'
    
    print 'saved'
    
    edTIME = time.clock() - stTIME
    print edTIME
    
    
    winsound.Beep(500, 800)
    
    return rTH