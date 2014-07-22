from __future__ import division
from pyteomics import mgf

#import copy
import pandas as pd
import re


inputfile = r'samples/C1.mgf'
outmgf = 'samples/C1-filtered-AorB.mgf'

outHead = r'samples/C1-Head.csv'
outSpec = r'samples/C1-Spec-frag.csv'

rTH = 0.01
biotin_tag = 'ARP'

delta = 0.8
a = 227.0854
b = 332.1387
c = 299.1127
d = 259.1223	
nl = 331.1314

#fragList = [a,b,c,d,nl]
#FRAG_List = [a,b,c,d]
NL_List = [nl]
FRAG_List = [a,b]
##############Settings finished ################
Head_pd = pd.DataFrame()
Spec_pd = pd.DataFrame()

with mgf.read(inputfile) as spectra:
    #header = mgf.read_header(inputfile)
    #reader = mgf.read('samples/C1.mgf')
    for reader in spectra:
        #reader_info = {}
        #reader_info = dict(reader)
        #auxiliary.print_tree(reader)
        #print reader['params']
        
        # #reader['params'] is a dict# #
        tmp_header = reader['params']
        reader_info = {'params':reader['params'],
                        'm/z array': reader['m/z array'],
                        'intensity array': reader['intensity array']}
        # # tmp_header['pepmass'] & tmp_header['charge'] are List, read data out# #
        pepinfo =  tmp_header['pepmass']
        #print pepinfo
        pepMZ = pepinfo[0]
        pepI = pepinfo[1]
        CHGinfo =  tmp_header['charge']
        CHG = CHGinfo[0]

        # calculation of peptide mass
        if CHG == 2 or CHG == r'2+':
            pepMZcalc = (pepMZ * 2) - (2 * 1.00783)
        elif CHG == 3 or CHG == r'3+':
            pepMZcalc = (pepMZ * 3) - (3 * 1.00783)
        elif CHG == 4 or CHG == r'4+':
            pepMZcalc = (pepMZ * 4) - (4 * 1.00783)
        elif CHG == 5 or CHG == r'5+':
            pepMZcalc = (pepMZ * 5) - (5 * 1.00783)
        else:
            pepMZcalc = pepMZ - 1.00783       
                        
        #print pepMZ, pepI
        # # format the dict to fit to Pandas DataFrame# #
        #tmp_header.pop('pepmass')
        #tmp_header['pepMZ'] = pepMZ 
        #tmp_header['pepI'] = pepI
        #tmp_header.pop('charge')
        #tmp_header['CHG'] = CHG
        #tmp_header['pepMZcalc'] = pepMZcalc
               
        #print tmp_header['title']
        x = tmp_header['title']
        y = x.strip(" \" ")
        ScanID = re.compile(r'=')
        ID = ScanID.split(y)
        ScanID = ID[-1]
        #ScanID = 'ScanID ' + str(ScanID)
        #tmp_header.pop('title')
        # print reader['intensity array']
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
        
        temp_FRAG_pd = pd.DataFrame()
        temp_NL_pd = pd.DataFrame()
        temp_found_pd = pd.DataFrame()
        # # intensity filter# #
        absTH = rTH * i_max
        #print 'absTH',absTH
        tmpSpec_pd_TH = tmpSpec_pd[tmpSpec_pd.i >= absTH]
        #tmpSpec_pd_TH.tail(3)
        
        # # fragment hunter # #
        for FRAG in FRAG_List:
            frag_L = FRAG-delta
            frag_H = FRAG+delta
            try:
                temp_query = str(frag_L) + r'<= mz <=' + str(frag_H)
                temp_query_info = tmpSpec_pd_TH.query(temp_query)
                #print ScanID,'',temp_query_info
                if temp_query_info.index.tolist() >0:
                    temp_FRAG_pd = temp_FRAG_pd.append(temp_query_info)
                else:
                    pass
            except:
                break
        
        #for NL in NL_List:
        #    NL_L = (pepMZcalc-nl)/CHG-delta
        #    NL_H = (pepMZcalc-nl)/CHG+delta
        #    
        #    temp_query = str(NL_L) + r'<= mz <=' + str(NL_H)
        #    temp_query_NL = tmpSpec_pd_TH.query(temp_query)
        #    count_NL = temp_query_NL.index.tolist()
        #    if len(count_NL) >0:
        #        temp_NL_pd = temp_NL_pd.append(temp_query_NL)
        #        print '<--NL  FOUND --->',ScanID
        #        print temp_NL_pd
        temp_found_pd = temp_found_pd.append(temp_FRAG_pd)
            #temp_found_pd = temp_found_pd.append(temp_NL_pd)
        
        
        #Spec_pd = Spec_pd.append(tmpSpec_pd)
        #Spec_pd = Spec_pd.append(temp_FRAG_pd)
        #Spec_pd.index.name = 'ion_count'
        #print tmpHead_pd
        #print tmpSpec_pd.head(5) 
        #spectra = mgf.read()
        count = temp_found_pd['mz'].tolist()
        if len(count) >0:
            print '#',len(count),'=',ScanID,'=',count
        if len(count) >0:
            #print temp_found_pd
            #print '++++++++++'
            #print reader['params']
            #print reader_info['params']
            mgf.write(reader_info, output= outmgf,header='')
        else:
            #print 'No Frag/NL found',ScanID
            pass
        
        
                                                                    

#print Head_pd.head(10)
#Head_pd.to_csv(outHead)
print 'finished'
#print Spec_pd.head(10)
#print Spec_pd.tail(10)
#Spec_pd.to_csv(outSpec)
#print 'finished'

print 'saved'

import winsound
winsound.Beep(500, 800)