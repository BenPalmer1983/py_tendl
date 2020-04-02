CROSS SECTIONS FOR PYTHON
====================================

Why?  The TENDL library is massive (30 GB unzipped p+n+d) and I only wanted the MF=3.  The compressed files are ~20MB.


The data was taken from TENDL-n

https://tendl.web.psi.ch/tendl_2019/talys.html


Only MF=3  (reaction cross sections)

Only MT:
                p n nu
           2:  [0,0,0],
           3:  [0,0,0],
           4:  [0,1,1],
           11: [1,3,4],
           16: [0,2,2],
           17: [0,3,3],
           22: [2,3,5],
           23: [6,7,13],
           24: [2,4,6],
           25: [2,5,7],
           28: [1,1,2],
           29: [2,4,6],
           30: [4,6,10],
           32: [1,2,3],
           33: [1,3,4],
           34: [2,2,4],
           35: [5,6,11],
           36: [5,7,12],
           37: [0,4,4],
           41: [1,2,3],
           42: [1,3,4],
           44: [2,1,3],
           45: [3,3,6],

The ENDF files have been read into python dictionaries (only the MF=3 and listed MT above).  The dictionaries are then converted to JSON and compressed into *.z files (extension irrelevant) using zlib in python.

To read a cross section from a file:

1. Import the tendl class from the tendl file
2. know the dir that stores the *.z files
3. projectile protons + neutrons  (1,0 for protons, 0,1 for neutrons, 1,1 for deuterons)
4. target protons and nucleons
5. residual protons and nucleons


from tendl import tendl
xs = tendl.read_xs(xs_dir, projectile_protons, projectile_neutrons, target_protons, target_nucleons, residual_protons, residual_nucleons)



