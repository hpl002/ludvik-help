# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:16:14 2021

@author: ludvi
"""

import os

Path = "C:/Users/ludvi/SIMA Workspaces/INOWINDMOOR12MW_BaseCase/Results"
filelist = os.listdir(Path)

for i in filelist:
    if i.endswith('.hdf5'):
        try:
            with open(Path + i, "r") as f:
                print(i)
        except:
            pass    
    
    print(f)

def readcol(filename,ignore,colnbr): #ignore = skip lines that starts with this sign, read colnbr 
    
    data=[]
    
    myfile=open(filename,'r')
    for line in myfile:
        if line[0]!=ignore:
            a=line.split()
            if 5.0>=float(a[1])>=1.0:   #read data between time 200s and 1800s
                data.append(float(a[colnbr]))
    myfile.close()
    return data

#def readlinetension():
#    
#    data = []
#    
#    for line in linetensions:
#        if line > :
            

from read_riflex_h5file import read_resfile
            
def fatigue_calculations_moorchain(OD,forces_file,colzf):
#OD = Mooring chain dimension, diameter of one leg of chain
#forces_file file name with axial forces
#colzf column number for axial forces on forces_file (Python numbering, starting at 0)
        
    resfile =

    #Coordinate system different from 3dfloats intertial sytem
    t=readcol(moments_file,'%',1)
    dt=t[1]-t[0]

#    Fz_col=readcol(forces_file,'%',colzf) ## Read mooring line axial force
    
    Fz=np.array(Fz_col)
    
    ## Cross section area for chain
    
    A = 2*np.pi/4.*OD**2 
    
    
    ## Axial stress
    sigmax = Fz/A ## [Pa]
        
   
   ## thickness, reference thickness and k are default values for mooring
    dsx = fatiguedamage_twoslope(t,sigmax,m1,loga1,m2,loga2,Nlim)


    print('Partial fatigue damage (axial stress) for chain: %.5e,' %(dsx))


    return dsx