# paper-aspect-melt-paper-2-data

This repository accompanies the paper
```
A new formulation for coupled magma/mantle dynamics
by Juliane Dannberg, Rene Gassmöller, Ryan Grove, and Timo Heister
```

and contains data files and code to reproduce the computations of the paper.

Contents
--------

TODO

Instructions
------------

install ASPECT:
...

The results in Section *3.1 1D analytical solution for the interface between regions with and without melt*
can be reproduced using the files in folder [arbogast-2017-benchmark](https://github.com/tjhei/paper-aspect-melt-paper-2-data/arbogast-2017-benchmark). 
This folder includes the code that is needed to run the models, the data files that were produced in the simulations, and script to plot the results as in Figure 3. 
To run the models, the plugin has to be compiled by running `ccmake .` in the arbogast-2017-benchmark folder and linking it to an ASPECT build directory. It can then be run using the input file `1d_arbogast_test`. 
Executing the bash script run.sh (`bash run.sh`) runs the model for the four different resolutions presented in the manuscript and writes the output into data files. These results can be plotted using a python script by executing `python ./plot_convergence.py`. All data files required to reproduce Figure 3 are included in the folder. 
