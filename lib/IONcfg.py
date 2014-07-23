import pandas as pd

class CFGparser:
    
    """
    CFGread: read ion config.csv direcly.
    CFGtype: read only one type of ion. (only Fragment/ only NL)
    CFGscore: read by the score/rank
    CFGquery: search certain FRAG/NL in certain score range
    
    all functions retrun a pandas DataFrame 
    """
    
    def __init__(self, csvNAME):
        self.csvNAME = csvNAME
    
    def CFGread(self):
            print 'Use config file: ', self.csvNAME
            
            self.cfg_df = pd.read_csv(self.csvNAME, sep=',', header=0, index_col=None)
            
            return self.cfg_df
            
    def CFGtype(self,TYPE):
        
        TYPE_list = ['F','FRAG','N','NL']
        
        if TYPE in TYPE_list:
            
            print 'Use config file: ', self.csvNAME
            self.cfg_df = pd.read_csv(self.csvNAME, sep=',', header=0, index_col=None)
            self.cfg_df_type = self.cfg_df[self.cfg_df['ionTYPE']==TYPE]
        
        return self.cfg_df_type
        
    def CFGscore(self,ionScore, ionScore2= None):
        
        if ionScore2 == None:
            print 'Use config file: ', self.csvNAME
            self.cfg_df = pd.read_csv(self.csvNAME, sep=',', header=0, index_col=None)
            self.cfg_df_score = self.cfg_df[self.cfg_df['ionScore']>=ionScore]
        
        else:
            print 'Use config file: ', self.csvNAME
            self.cfg_df = pd.read_csv(self.csvNAME, sep=',', header=0, index_col=None)
            
            ionScoreA = min(ionScore, ionScore2)
            ionScoreB = max(ionScore, ionScore2)
            
            temp_query = str(ionScoreA) + r'<= ionScore <=' + str(ionScoreB)
            
            self.cfg_df_score = self.cfg_df.query(temp_query)
        
        return self.cfg_df_score
        
    def CFGquery(self,TYPE=None,ionScore=None, ionScore2= None):
        
        TYPE_list = ['F','FRAG','N','NL']
        print 'Use config file: ', self.csvNAME
        self.cfg_df = pd.read_csv(self.csvNAME, sep=',', header=0, index_col=None)
        
        if ionScore!=None and ionScore2 == None:
            if TYPE in TYPE_list:               
                self.cfg_df_query = self.cfg_df[self.cfg_df['ionScore']>=ionScore]
                self.cfg_df_query = self.cfg_df_query[self.cfg_df_query['ionTYPE']==TYPE]
            else:
                self.cfg_df_query = self.cfg_df[self.cfg_df['ionScore']>=ionScore]
        
        elif ionScore!=None and ionScore2 != None:        
            ionScoreA = min(ionScore, ionScore2)
            ionScoreB = max(ionScore, ionScore2)
            if TYPE in TYPE_list: 
                temp_query = str(ionScoreA) + r'<= ionScore<=' + str(ionScoreB) + ' and ' + 'ionTYPE==\"'+ TYPE + '\"'
                
                self.cfg_df_query = self.cfg_df.query(temp_query)
            else:
                temp_query = str(ionScoreA) + r'<= ionScore <=' + str(ionScoreB)
                self.cfg_df_query = self.cfg_df.query(temp_query)
                
        return self.cfg_df_query