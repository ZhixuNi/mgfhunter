from pyteomics import mgf

spectra = mgf.read(r'samples/C1Copy.mgf')
outmgf = 'C1r4.mgf'
for reader in spectra:
    print reader
    print '=========================='
    x = reader
    
    mgf.write(spectra = x, output = outmgf, header='')