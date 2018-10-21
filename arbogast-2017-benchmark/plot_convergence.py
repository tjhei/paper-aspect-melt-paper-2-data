#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib.path import Path
import matplotlib.patches as patches

prop={'size':12}
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = '\usepackage{relsize}'
plt.rc('font', family='sanserif')
fig=plt.figure(dpi=200,figsize=(15,4.5)) 

# ndofs,u,p,p_f,p_c,phi,u_f
file_name=["convergence_results_old","convergence_results_new","convergence_results_arbogast"]
labels=["Dannberg \& Heister, 2016", "new formulation", "Arbogast et al., 2017"]

# Velocity error
plt.subplot(131)
data = []
for j in range(0,len(file_name)):
	data = (np.genfromtxt(str(file_name[j]), delimiter=' ', dtype = float))
	plt.loglog(data[:,0],abs(data[:,1]),color=colors.color(j+3), marker=colors.marker(j),label=labels[j], markersize=10)

plt.loglog(data[:,0],abs(0*data[:,1]+(data[0,1])/(8e-4*data[:,0]*data[:,0])),color='k', marker=colors.marker(j),label="quadratic convergence", markersize=1, linestyle='--')

plt.xlim([10, 300])
plt.ylim([1e-8, 1e-4])
plt.xlabel("\#cells")
plt.ylabel("$L_2$ velocity error")

plt.legend(loc = "upper left", ncol=1, prop=prop)

# Fluid pressure error
plt.subplot(132)
data = []
for j in range(0,len(file_name)):
	data = (np.genfromtxt(str(file_name[j]), delimiter=' ', dtype = float))
	plt.loglog(data[:,0],abs(data[:,2]),color=colors.color(j+3), marker=colors.marker(j), markersize=10)

plt.loglog(data[:,0],abs(0*data[:,2]+(data[0,2])/(6e-4*data[:,0])),color='k', marker=colors.marker(j),label="linear convergence", markersize=1, linestyle='--')

plt.xlim([10, 300])
plt.ylim([1e-4, 1])
plt.xlabel("\#cells")
plt.ylabel("$L_2$ fluid pressure error")

plt.legend(loc = "upper left", ncol=1, prop=prop)

# Compaction pressure error
plt.subplot(133)
data = []
for j in range(0,len(file_name)-1):
	data = (np.genfromtxt(str(file_name[j]), delimiter=' ', dtype = float))
	plt.loglog(data[:,0],abs(data[:,3]),color=colors.color(j+3), marker=colors.marker(j), markersize=10)

plt.loglog(data[:,0],abs(0*data[:,3]+(data[0,3])/(1e-1*data[:,0])),color='k', marker=colors.marker(j),label="linear convergence", markersize=1, linestyle='--')

plt.xlim([10, 300])
plt.ylim([5e-5, 0.05])
plt.xlabel("\#cells")
plt.ylabel("$L_2$ compaction pressure error")
 
plt.legend(loc = "upper left", ncol=2, prop=prop)

plt.savefig('arbogast_error_plot.pdf', #bbox_extra_artists=(legend,), 
            bbox_inches='tight',dpi=200)

