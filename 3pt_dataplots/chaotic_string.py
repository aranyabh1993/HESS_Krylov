#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:11:13 2024

@author: aneekphys
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from lanczos_tfd import *


##------------ Level Statistics ---------------

'''

# N=400

r_f = [] # restricted ratios

for k in range(1000):
    
    data = np.loadtxt(f'N_400_roots/set_{k+1}.txt') # the original data is in the range 0 to 0.5
    
    data = [4*root for root in np.sort(data) if root > 0] # convert the data to be in 0 to 2, like RMT
    
    rr = list(restricted_ratios(data))
    
    r_f += rr
    
    
plot_restricted_ratios(r_f, 'string scattering, N=400')
plt.savefig('level_stat_string_scattering_N=400.pdf')
 
# N=800   
    
r_f = [] # restricted ratios

for k in range(1000):
    
    data = np.loadtxt(f'N_800_roots/set_{k+1}.txt') # the original data is in the range 0 to 0.5
    
    data = [4*root for root in np.sort(data) if root > 0] # convert the data to be in 0 to 2, like RMT
    
    rr = list(restricted_ratios(data))
    
    r_f += rr
    
    
plot_restricted_ratios(r_f, 'string scattering, N=800')
plt.savefig('level_stat_string_scattering_N=800.pdf')


# N=1000   
    
r_f = [] # restricted ratios

for k in range(4000):
    
    data = np.loadtxt(f'N_1000_roots/set_{k+1}.txt') # the original data is in the range 0 to 0.5
    
    data = [(8*root-2) for root in np.sort(data) if root > 0] # convert the data to be in -2 to 2, like RMT
    
    rr = list(restricted_ratios(data))
    
    r_f += rr
    
    
plot_restricted_ratios(r_f, 'string scattering, N=1000')
plt.savefig('level_stat_string_scattering_N=1000.pdf')


# N=1600   
    
r_f = [] # restricted ratios

for k in range(2000):
    
    data = np.loadtxt(f'N_1600_roots/set_{k+1}.txt') # the original data is in the range 0 to 0.5
    
    data = [(8*root-2) for root in np.sort(data) if root > 0] # convert the data to be in -2 to 2, like RMT
    
    rr = list(restricted_ratios(data))
    
    r_f += rr
    
    
plot_restricted_ratios(r_f, 'string scattering, N=1600')
plt.savefig('level_stat_string_scattering_N=1600.pdf')


########-------------------------x--------------------------------------
'''    
 

 
## Complexity calculation
 
# N=400

tlist = np.arange(0,5,0.01)
complexity = np.zeros(len(tlist))
M=500


for m in range(M):
    
    k = np.random.randint(1000)
    
    data_400 = np.loadtxt(f'N_400_roots/set_{k+1}.txt')
    
    # convert the data to be in -2 to 2, like RMT

    data = [(8*root-2) for root in np.sort(data_400) if root > 0] # convert the data to be in -2 to 2, like RMT

    tf = 1*5*len(data)
    dt = 1*0.01*len(data)


    complexity += (complexity_tfd_full(data,0, tf, dt)['KCOMPLEXITY']/len(data))/M
 


np.savetxt('complexity_N_400_tf_5.txt',complexity)


plt.figure()

plt.plot(tlist,complexity)

plt.xlabel(r't/L',fontsize=12)
plt.ylabel(r'C(t)/L',fontsize=12)
plt.title('String Scattering, N=400')

plt.show()

plt.savefig('complexity_N_400_tf_5.pdf')

print('done N=400\n')


 
# N=800

tlist = np.arange(0,5,0.01)
complexity = np.zeros(len(tlist))
M=500


for m in range(M):
    
    k = np.random.randint(1000)
    
    data_800 = np.loadtxt(f'N_800_roots/set_{k+1}.txt')

    data = [(8*root-2) for root in np.sort(data_800) if root > 0] # convert the data to be in -2 to 2, like RMT

    tf = 1*5*len(data)
    dt = 1*0.01*len(data)


    complexity += (complexity_tfd_full(data,0, tf, dt)['KCOMPLEXITY']/len(data))/M
 


np.savetxt('complexity_N_800_tf_5.txt',complexity)


plt.figure()

plt.plot(tlist,complexity)

plt.xlabel(r't/L',fontsize=12)
plt.ylabel(r'C(t)/L',fontsize=12)
plt.title('String Scattering, N=800')

plt.show()

plt.savefig('complexity_N_800_tf_5.pdf')

print('done N=800\n')


# N=1000

tlist = np.arange(0,5,0.01)
complexity = np.zeros(len(tlist))
M=500


for m in range(M):
    
    k = np.random.randint(4000)
    
    data_1000 = np.loadtxt(f'N_1000_roots/set_{k+1}.txt')

    data = [(8*root-2) for root in np.sort(data_1000) if root > 0] # convert the data to be in -2 to 2, like RMT

    tf = 1*5*len(data)
    dt = 1*0.01*len(data)


    complexity += (complexity_tfd_full(data,0, tf, dt)['KCOMPLEXITY']/len(data))[0:len(complexity)]/M
 


np.savetxt('complexity_N_1000_tf_5.txt',complexity)


plt.figure()

plt.plot(tlist,complexity)

plt.xlabel(r't/L',fontsize=12)
plt.ylabel(r'C(t)/L',fontsize=12)
plt.title('String Scattering, N=1000')

plt.show()

plt.savefig('complexity_N_1000_tf_5.pdf')

print('done N=1000\n')


# N=1600

tlist = np.arange(0,5,0.01)
complexity = np.zeros(len(tlist))
M=500


for m in range(M):
    
    k = np.random.randint(2000)
    
    data_1600 = np.loadtxt(f'N_1600_roots/set_{k+1}.txt')

    data = [(8*root-2) for root in np.sort(data_1600) if root > 0] # convert the data to be in -2 to 2, like RMT

    tf = 1*5*len(data)
    dt = 1*0.01*len(data)


    complexity += (complexity_tfd_full(data,0, tf, dt)['KCOMPLEXITY']/len(data))/M
 


np.savetxt('complexity_N_1600_tf_5.txt',complexity)


plt.figure()

plt.plot(tlist,complexity)

plt.xlabel(r't/L',fontsize=12)
plt.ylabel(r'C(t)/L',fontsize=12)
plt.title('String Scattering, N=1600')

plt.show()

plt.savefig('complexity_N_1600_tf_5.pdf')


print('done N=1600\n')





