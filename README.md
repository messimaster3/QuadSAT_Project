# QuadSAT_Project
QuadSat project in DM884 Autonomous Unmanned Aerial Vehicles

This program is only designed to work, with the filestrucktur from Quadsat

This a program that can show cvs files in 3d. 
The program was original designed to view RosBag files, however to my seaching that is no python model that can convert a ROSbag to a CSV file.
This can however be done very easy on ubuntu just using the command : rostopic echo -b FILE -p /FCU/GPS_Int_Data > FILENAME.csv

Example of command:
rostopic echo -b drone_2021-09-15-21-54-36.bag -p /FCU/GPS_Int_Data > drone_2021-09-15-21-54-36.csv


## How to run:

Install all dependencies from the requirements.txt, this can be done via pip.

When all dependencies are installed, type: "python GUI.py" to run the program

### NOTE: 
All errors are printed to the terminal

## Quick use:

I the user just what to the view some csv files in the program, some csv files can be found in the repository under dataFiles/cvsFiles
The original ROSbag files to the csv files is found in the bagFiles.