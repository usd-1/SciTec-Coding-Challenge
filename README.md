<h1 align="center">SciTec-Coding-Challenge</h1>
<p align="center"><strong>LLA to ECEF</strong>
<br>Deals with a LLA time series and converts to ECEF for velocity calculation using linear interpolation.</p>
<br/>
<h2>About</h2>
  In the field of remote sensing, a common task that comes up is coordinate conversion. Two common coordinate systems are geodetic coordinates, consisting of     latitude, longitude, and altitude (LLA) and geocentric coordinates measured in degrees, also called Earth-centered, Earth-fixed (ECEF) shown in meters.

<h2>Goal</h2>
The idea behind the implementation of this code was to solve 4 problems with a given time series dataset.

1. Read the CSV file located in the 'dataset' folder, which is a dataset that represents a time series of an object using LLA coordinates. 
2. Convert the LLA coordinates to ECEF coordinates
3. Calculate ECEF velocity at the time points given in the input file and export them as a csv file called "ECEF Velocities" under 'dataset' folder.
4. Interpolate ECEF velocity for any requested time. This program should call the function or class created, and evaluate the ECEF velocity vector at two specific times: '1532334000' and '1532335268'. The result should be printed to stdout for both of the given times. 

<h2>Required Versions</h2>
- Python 3
- pandas 1.1.4
- numpy 1.8.2
- scipy 1.19.3

<h2>Steps of Execution</h2>

1. Download this project as zip
2. Check that you have all required versions listed. 
3. Source src_main.py

<h2>Output Details</h2>

1. Results from goal 3 are stored in the dataset directory hosted on the root directory. 
2. Results from goal 4 are printed as stdout on console.

<h2>Project status</h2>
Finished 12/02/2020

<h2>Credits</h2>

- Author:Uma S Dixit

<h2>Copyright</h2>
This project is licensed under the terms of the MIT license and protected by Udacity Honor Code and Community Code of Conduct.
