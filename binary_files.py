import numpy as np
import sys
import subprocess
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.plotly as py
from matplotlib import cm

#Files input

level=np.zeros((2,2))
nlevel=int(input("Number of level "))
test=np.full((2,200), False)
valuereal=np.zeros((2,200))
logplot=[]

for i in range(0,2):    
    logplot.append('')

for i in range(0,2):

    logplot[i]=input("MD data or experimental data? [MD/exp] ")

    if(logplot[i].lower()=='md'):
        name1=input("Enter name file MD ")
        file1=open(name1,'r')
        k=-1
        for line in file1:
            value=float(line)
            k=k+1
            valuereal[i,k]=value
            test[i,k]=True
        file1.close()
        ktot=k+1

        
    else:
        name1=input("Enter name file exp data ")
        file1=open(name1,'r')
        k=-1
        for line in file1:
            value=float(line)
            k=k+1
            valuereal[i,k]=value
            #print(i,k,valuereal[i,k])
            if(value > -0.0001):
                test[i,k]=True
            
        file1.close()
        ktot=k+1
    for j in range(0,nlevel):
        level[i,j]=float(input("Enter level  "+str(j+1)+'-th '))

for i in range(0,2):
    if(logplot[i].lower()=='md'):
        fileout1=input("MD output name ")
      
    else:
        fileout1=input("exp output name ")
    file1=open(fileout1,'w')
    for j in range(0,ktot):
        if(test[0,j] == True and test[1,j] == True):
            logtest=False
            for t in range(0,nlevel):
                if(valuereal[i,j] < level[i,t]):
                    logtest=True
                    aa1=t
                    out1='%5d'%aa1+'\n'
                    file1.write(out1)
                    break
            if(logtest==False):
                aa1=nlevel
                out1='%5d'%aa1+'\n'
                file1.write(out1)
    file1.close()
