import os
import csv

class IO_input():
    
    """ 
    All functions required for file IO of mzML file
    """
    
    def __init__(self, input_PATH = None ):
        self.input_PATH = input_PATH
        self.File_type = '.mzML'
    
    def inputFATH(self):
        """ 
        Check if input is correct, give file name and path of input file
        """
        x = self.input_PATH
        infile_info =[]
        if os.path.isabs(x):
            if os.path.exists(x):
                if os.path.isfile(x):
                    (PATH, NAME) = os.path.split(x)
                    infile_info = [PATH, NAME]
                    print 'PATH', PATH
                    print 'NAME',NAME
                else:
                    NAME = ''
            else:
                NAME = ''
        else:
            try:
                xx = os.path.abspath(x)
                
                
                (PATH, NAME) = os.path.split(xx)
                infile_info = [PATH, NAME]
                print infile_info
                print 'PATH', PATH
                print 'NAME',NAME
                    
            except:
                print 'NOT abs PATH',x
                PATH = 'NO PATH'
                NAME = ''
    
    
        if NAME != '':
            try:
                #NAME_short = NAME.rstrip('.mzML')
                print NAME
                (NAME_short,NAME_type) = os.path.splitext(NAME)
                if NAME_type == self.File_type:
                    infile_info = [NAME,PATH,NAME_short,NAME_type]
                else:
                    print 'NOT .mzML file'
                    infile_info = []
                    
            except:
                print 'NOT .mzML file'
                infile_info = []
                
        if len(infile_info) == 4:
            pass
        else:
            infile_info = ['','','','']
            
        return infile_info
        

class IO_MS1Array():
    
    """ 
    All functions required for file IO to dump MS1ArrayMS2Array file
    """
    
    def __init__(self, get_PATH = None):
        self.get_PATH = get_PATH
        self.NAME_type = '.csv'        
    def MS1wirter(self, ROWS):
        
        MS1Array = open(self.get_PATH, 'wb')
        writer1 = csv.writer(MS1Array)
        writer1.writerows(ROWS)
        MS1Array.close()           
        

class IO_MS2Array():
    
    """ 
    All functions required for file IO to dump MS2Array file
    """
    
    def __init__(self, get_PATH = None):
        self.get_PATH = get_PATH
        self.NAME_type = '.csv'
        
        
    def MS2wirter(self, ROWS):
        MS2Array = open(self.get_PATH, 'wb')
        writer2 = csv.writer(MS2Array)
        writer2.writerows(ROWS)
        MS2Array.close()       

        
class IO_output():
    
    """ 
    All functions required for file IO to dump MS1ArrayMS2Array file
    """
    
    def __init__(self, get_PATH = None):
        self.get_PATH = get_PATH
        self.NAME_type = '.csv'        
    def outputwirter(self, ROWS):
        output = open(self.get_PATH, 'wb')
        writer_o = csv.writer(output)
        writer_o.writerows(ROWS)
        output.close() 
        
        
        
class IO_tmp():

    """ 
    All functions required to delete all unnecessary tempory files
    """
    
    def __init__(self, get_PATH = None):
        self.get_PATH = get_PATH
    
    def deltmp (self):
        """ 
        Check if temp file path is exist and delete it
        """
        x = self.get_PATH
        if os.path.exists(x):
            if os.path.isfile(x):
                print 'is ABS PATH'
                if os.path.isabs(x):
                    os.remove(x)
                    print 'file removed'
                    

