# paper-aspect-melt-paper-2-data

This repository accompanies the paper
```
A new formulation for coupled magma/mantle dynamics
by Juliane Dannberg, Rene Gassmöller, Ryan Grove, and Timo Heister
```

and contains data files and code to reproduce the computations of the paper.

Contents
--------

- Input files and code to reproduce the 1-D test case from Arbogast et al., 2017
- Input and data files to reproduce the 2-D mid-ocean ridge model
- Input and data files to reproduce the 3-D transform fault model

Instructions
------------

The first step for reproducing the results is installing ASPECT, or using a docker image or virtual machine. 
Instructions are provided in the [ASPECT manual](http://www.math.clemson.edu/%7Eheister/manual.pdf).

The results in Section *3.1 1-D analytical solution for the interface between regions with and without melt*
can be reproduced using the files in folder [arbogast-2017-benchmark](https://github.com/tjhei/paper-aspect-melt-paper-2-data/tree/master/arbogast-2017-benchmark). 
This folder includes the code that is needed to run the models, the data files that were produced in the simulations, and a script to plot the results as in Figure 3. 
To run the models, the plugin has to be compiled by running `ccmake .` in the arbogast-2017-benchmark folder and linking it to an ASPECT build directory. It can then be run using the input file `1d_arbogast_test.prm`. 
Executing the bash script run.sh (`bash run.sh`) runs the model for the four different resolutions presented in the manuscript and writes the output into data files. These results can be plotted using a python script by executing `python ./plot_convergence.py`. All data files required to reproduce Figure 3 are included in the folder. 

The results in Section *3.2 Numerical results: 2-D mid-ocean ridge model* and *3.3
3-D Application: Oceanic transform fault*
can be reproduced using the files in folder [mid-ocean-ridge](https://github.com/tjhei/paper-aspect-melt-paper-2-data/tree/master/mid-ocean-ridge). The results in the manuscript were produced using the version of ASPECT in branch [https://github.com/jdannberg/aspect/tree/melt_viscosity_range](https://github.com/jdannberg/aspect/tree/melt_viscosity_range). 
The input files for the different setups are located in the `input_files` folder, and they can be run as any other aspect model by executing `/path-to-aspect-build-directory/aspect ./name-of-input-file.prm`. The models have to be run in the `input_files` folder, as the location of the data files required to run the models is only given as a relative path. 
To reproduce the results in Figure 8, all `mid_ocean_ridge*` input files have to be run. 
The `mid_ocean_ridge_ascii_data.prm` and `mid_ocean_ridge_compaction_length.prm` were run several times 
to produce the different data points. 

For the global refinement series, given in the input file `mid_ocean_ridge_ascii_data.prm`, the global refinement was varied 
between 4 and 10. This can be reproduced by modifying the line
`set Initial global refinement = 8` 
to the desired value. 

For the refinement based on compaction legth, given in the input file `mid_ocean_ridge_compaction_length.prm`, the 
number of mesh cells per compaction length were varied, using values of 1, 2, 4, 8, 16 and 32. 
This can be reproduced by modifying the line
`set Mesh cells per compaction length = 32` 
to the desired value. 

For all other models, the data points in Figure 8 come from the different adaptive refinement levels, 
and graphical and statistics output is produced for each of them in a single run of the model. 

The transform fault model can be reproduced by using the input file `transform_fault_hires.prm`. 

