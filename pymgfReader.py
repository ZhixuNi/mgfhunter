from pyteomics import mgf
import pandas as pd
import re

fileNAME = 'PC-IM-1st-filtered-3key-rTH0.1'
inputfile = 'samples/'+fileNAME+'.mgf'

outHead = 'samples/'+fileNAME+'-Head.csv'
outSpec = 'samples/'+fileNAME+'-Spec.csv'
Head_pd = pd.DataFrame()
Spec_pd = pd.DataFrame()

with mgf.read(inputfile) as spectra:
    #reader = mgf.read('samples/C1.mgf')
    for reader in spectra:
        #auxiliary.print_tree(reader)
        #print reader['params']
        
        # #reader['params'] is a dict# #
        tmp_header = reader['params']
        
        # # tmp_header['pepmass'] & tmp_header['charge'] are List, read data out# #
        pepinfo =  tmp_header['pepmass']
        #print pepinfo
        pepMZ = pepinfo[0]
        pepI = pepinfo[1]
        try:
            CHGinfo =  tmp_header['charge']
            #print reader['params']
            CHG = CHGinfo[0]
        except KeyError:
            CHG = 'X'
            tmp_header['charge'] = CHG
        
        #print pepMZ, pepI
        # # format the dict to fit to Pandas DataFrame# #
        tmp_header.pop('pepmass')
        tmp_header['pepMZ'] = pepMZ 
        tmp_header['pepI'] = pepI
        tmp_header.pop('charge')
        tmp_header['CHG'] = CHG
        
        #print tmp_header['title']
        x = tmp_header['title']
        y = x.strip(" \" ")
        ScanID = re.compile(r'=')
        ID = ScanID.split(y)
        ScanID = ID[-1]
        #ScanID = 'ScanID ' + str(ScanID)
        tmp_header.pop('title')
        # print reader['intensity array']
        LS_lenth = len(reader['m/z array'])
        ScanID_List = [ScanID]*LS_lenth
        
        tmp_spec = {'ScanID': ScanID_List,
                    'm/z': reader['m/z array'],
                    'i': reader['intensity array']}
    
        tmpHead_pd = pd.DataFrame (tmp_header, index = [ScanID], columns=['pepMZ', 'pepI', 'CHG', 'rtinseconds'])
        Head_pd = Head_pd.append(tmpHead_pd)
        Head_pd.index.name = 'ScanID'
        
        tmpSpec_pd = pd.DataFrame(tmp_spec,columns=['ScanID','m/z', 'i'])
        Spec_pd = Spec_pd.append(tmpSpec_pd)
        Spec_pd.index.name = 'ion_count'
        #print tmpHead_pd
        #print tmpSpec_pd.head(5)                               

print Head_pd.head(10)
Head_pd.to_csv(outHead)
print Spec_pd.head(10)
Spec_pd.to_csv(outSpec)
print 'finished'