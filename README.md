# QuadSAT_Project
QuadSat project in DM884 Autonomous Unmanned Aerial Vehicles

This program is only designed to work, with the filestrucktur from Quadsat.

This a program that can show csv files in 3d.
The program was original designed to view RosBag files, however to my seaching that is no python model for python3, that can convert a ROSbag to a CSV file.
This can however be done very easy on Ubuntu just using this command : rostopic echo -b "BAGFILE" -p "topic" > "FILENAME.csv"

Example of command:
rostopic echo -b drone_2021-09-15-21-54-36.bag -p /FCU/GPS_Int_Data > drone_2021-09-15-21-54-36.csv


## How to run:

Install all dependencies from the requirements.txt, this can be done via pip.

When all dependencies are installed, type: "python3 GUI.py" to run the program

### NOTE: 
All errors for the program is printed to the terminal.

## Quick use:

If the user just what to the view some csv files in the program, some csv files can be found in the repository under dataFiles/cvsFiles
The original ROSbag files to the csv files is found in the bagFiles folder; dataFiles/RosBags.