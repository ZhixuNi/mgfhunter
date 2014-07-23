from pyteomics import mgf
import pandas as pd
import re

def RTreducer (inmgf,outmgf,RT1,RT2,unit=None):
    secList = ['S','s','Sec','sec']
    minList = ['M','m','Min','min']
    
    if unit == None:
        unit = 'sec'
        pass
    if unit in secList:
        pass
    if unit in minList:
        RT1 = float( RT1 * 60)
        RT2 = float( RT2 * 60)
    else:
        unit = 'sec'
        
    spectra = mgf.read(inmgf)
    for reader in spectra:
        tmp_header = reader['params']
        RT = float(tmp_header['rtinseconds'])
        if RT1 <= RT <= RT2:
            mgf.write(reader, output= outmgf,header='') 
        else:
            pass
            
    print 'mgfRTreducer --> Saved!'
    

def SCANtoCSV (inmgf,outcsv):
    
    Head_pd = pd.DataFrame()
    spectra = mgf.read(inmgf)
    for reader in spectra:
        tmp_header = reader['params']
        
        # # tmp_header['pepmass'] & tmp_header['charge'] are List, read data out# #
        pepinfo =  tmp_header['pepmass']
        pepMZ = pepinfo[0]
        pepI = pepinfo[1]
        # # some ion don't have charge info# #
        try:
            CHGinfo =  tmp_header['charge']
            CHG = CHGinfo[0]
        except KeyError:
            CHG = 'X'
            tmp_header['charge'] = CHG
        
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
    
        tmpHead_pd = pd.DataFrame (tmp_header, index = [ScanID], columns=['pepMZ', 'pepI', 'CHG', 'rtinseconds'])
        Head_pd = Head_pd.append(tmpHead_pd)
        Head_pd.index.name = 'ScanID'
    
    # # finish loop# #
    # # save output# #
    Head_pd.to_csv(outcsv)
    
    print 'SCANtoCSV -->Saved as: ',outcsv
    
    
def MS2toCSV (inmgf,outcsv):
    
    Spec_pd = pd.DataFrame()
    spectra = mgf.read(inmgf)
    for reader in spectra:

        x = reader['title']
        y = x.strip(" \" ")
        ScanID = re.compile(r'=')
        ID = ScanID.split(y)
        ScanID = ID[-1]

        # print reader['intensity array']
        LS_lenth = len(reader['m/z array'])
        ScanID_List = [ScanID]*LS_lenth
        
        tmp_spec = {'ScanID': ScanID_List,
                    'm/z': reader['m/z array'],
                    'i': reader['intensity array']}
    
        tmpSpec_pd = pd.DataFrame(tmp_spec,columns=['ScanID','m/z', 'i'])
        Spec_pd = Spec_pd.append(tmpSpec_pd)
        Spec_pd.index.name = 'ion_count'
        Spec_pd.index.name = 'ScanID'
    
    # # finish loop# #
    # # save output# #
    Spec_pd.to_csv(outcsv)
    
    print 'MS2toCSV -->Saved as: ',outcsv
        