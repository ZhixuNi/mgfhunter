# -*- coding: utf-8 -*-
#Copyright 2014 Zhixu Ni, AG Bioanalytik,BBZ,University of Leipzig            #
#The software is currently  under development and is not ready to be released.#
#A suitable license will be choosen before the offical release of mgfHunter.  #
#For more info please contact: zhixu.ni@uni-leipzig.de                        #

from pyteomics import mgf

spectra = mgf.read(r'samples/C1Copy.mgf')
outmgf = 'C1r4.mgf'
for reader in spectra:
    print reader
    print '=========================='
    x = reader
    
    mgf.write(spectra = x, output = outmgf, header='')