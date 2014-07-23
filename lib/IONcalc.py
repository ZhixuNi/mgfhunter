from __future__ import division

def IONmass (MASS, MASStype, pepMASS=None, prCHG=None, ionCHG=None):
      
         
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
        ionMZ = ((orignalMASS - MASS) + ionCHG * H)/ionCHG
    
    return ionMZ
    
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