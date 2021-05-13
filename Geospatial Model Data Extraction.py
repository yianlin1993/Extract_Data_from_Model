#!/usr/bin/env python
### This script is designed to extract modeling results to be compared against well measurement data
### Modeling results gives the predicted value in each geospatial grid but there are limited location of well measurements so this script extract the predicted value at the well site.

import csv
from csv import reader

wellsite='S8RD_PAC_01'  ### well measurements
DynTop = 'c200_07_L160_DynTop' ### modeling results
print(wellsite)
print(DynTop)

well_rows = list(reader(open(wellsite)))
DT_rows = list(reader(open(DynTop)))

well_rows[0].append(DynTop)
f = open('RD_DT_PAC_c200_L160', 'a')
f.write(str(well_rows[0]))
f.write('\n')

for row in well_rows[1:]:
    lon_input = row[0].split()[0]
    lat_input = row[0].split()[1]
    print(lon_input, lat_input)  ### well measurements location
    lon_dif = []
    lat_dif = []
    dep = []
    ### iterate through modeling results to create a list of the difference between well location and modeling grid
    for line in DT_rows:
            lon_dif.append(abs(float(line[0].split()[0])-float(lon_input)))
            lat_dif.append(abs(float(line[0].split()[1])-float(lat_input)))
            dep.append(float(line[0].split()[2]))
    latminindex = []
    for i in range(len(lat_dif)):
        if lat_dif[i] == min(lat_dif):
            latminindex.append(i)
    print(min(lat_dif))
    print(min(lon_dif))
    ###  find the index of the nearest grid to the well location
    n = lon_dif.index(min(lon_dif), min(latminindex), max(latminindex))
    print((float(lon_dif[n])+float(lon_input)), (float(lat_dif[n])+float(lat_input)), dep[n])
    row.append(dep[n])
    print(row)

    f.write(str(row))
    f.write('\n')
f.close()

