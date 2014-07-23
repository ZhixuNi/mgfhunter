from __future__ import division
from pyteomics import mgf
from lib.IONcalc import IONmass,PRmass
from lib.IONcfg import CFGparser
import pandas as pd
import re
import time

stTIME = time.clock()

inputfile = r'samples/PC-IM-1st.mgf'
outmgf = 'samples/PC-IM-1st-filtered-3key-rTH0.1.mgf'
cfgNAME = 'ionCFG_PL.csv'

#outHead = r'samples/C1-Head.csv'
#outSpec = r'samples/C1-Spec-frag.csv'

rTH = 0.1  # 0.01 = 1%
delta = 0.8

ScoreTH1 = 113.5
ScoreTH2 = 300.0
#biotin_tag = 'ARP'

#delta = 0.8
#a = 227.0854
#b = 332.1387
#c = 299.1127
#d = 259.1223	
#nl = 331.1314
#
##fragList = [a,b,c,d,nl]
##FRAG_List = [a,b,c,d]
#NL_List = [nl]
#FRAG_List = [a,b]


cfg = CFGparser(cfgNAME)

#TYPE = 'F'
Score1 = 10
cfg_df_q = cfg.CFGquery(ionScore=Score1)
print cfg_df_q

##############Settings finished ################
Head_pd = pd.DataFrame()
Spec_pd = pd.DataFrame()

with mgf.read(inputfile) as spectra:
    for reader in spectra:
        
        # #reader['params'] is a dict# #
        tmp_header = reader['params']
        reader_info = {'params':reader['params'],
                        'm/z array': reader['m/z array'],
                        'intensity array': reader['intensity array']}

        pepinfo =  tmp_header['pepmass']
        #print pepinfo
        pepMZ = pepinfo[0]
        pepI = pepinfo[1]
        try:
            CHGinfo =  tmp_header['charge']
            prCHG = CHGinfo[0]
        except KeyError:
            prCHG = 1
        RT = float(tmp_header['rtinseconds'])

        # calculation of peptide mass
        pepMZcalc = PRmass(pepMZ, prCHG)

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
    
        #tmpHead_pd = pd.DataFrame (tmp_header, index = [ScanID], columns=['pepMZ', 'pepI', 'CHG', 'pepMZcalc', 'rtinseconds'])
        #Head_pd = Head_pd.append(tmpHead_pd)
        #Head_pd.index.name = 'ScanID'
        
        tmpSpec_pd = pd.DataFrame(tmp_spec,columns=['ScanID','mz', 'i'])
        
        #temp_FRAG_pd = pd.DataFrame()
        #temp_NL_pd = pd.DataFrame()
        temp_ion_pd = pd.DataFrame()
        temp_found_pd = pd.DataFrame()
        tmp_found_List =[]
        # # intensity filter# #
        absTH = rTH * i_max
        #absTH = float(absTH)
        #print 'absTH',absTH
        
        tmpSpec_pd_TH = tmpSpec_pd[tmpSpec_pd['i'] >= absTH]
        #print tmpSpec_pd_TH, absTH
        #tmpSpec_pd_TH.tail(3)
        
        # # ion hunter # #
        #print '#',ScanID, '---->'
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
                            
                ion_L = ionMZ-delta
                ion_H = ionMZ+delta
                
    
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
        temp_ion_pd = pd.DataFrame()
                

print 'finished'

print 'saved'

edTIME = time.clock() - stTIME
print edTIME

import winsound
winsound.Beep(500, 800)