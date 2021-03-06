import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Takes the path to a csv file, reads the data and puts into 3 np arrays.
# Returns 3 np arrays
def readCSVFileAndPrep(path):
    latitude = []
    longitude = []
    relative_altitude = []

    data = pd.read_csv(path)
    latitude = np.concatenate((data[['field.latitude']].to_numpy()), axis=None)    
    longitude = np.concatenate((data[['field.longitude']].to_numpy()), axis=None)
    relative_altitude = np.concatenate((data[['field.relative_altitude']].to_numpy()), axis=None)

    print("Number of latitde datapoints " + str(len(latitude)))
    print("Number of longitude datapoints " + str(len(longitude)))
    print("Number of relative_altitude datapoints " + str(len(relative_altitude)))

    return latitude, longitude, relative_altitude

    # Takes a list and removes every second element in list (helper function to pruneDataSet)
    # Returns a list
def pruneList(listToPrune):
    return np.delete(listToPrune, np.arange(0, listToPrune.size, 2))

    # Takes the dataset and makes it half the size. The is done numberOfPrune times.
    # Returns 3 lists
def pruneDataSet(latitude, longitude, relative_altitude, numberOfPrune):
    
    print("Prune latitude")
    for x in range(numberOfPrune):
        pruned_latitude = pruneList(latitude)
        latitude = pruned_latitude

    print("Prune longitude")
    for x in range(numberOfPrune):
        pruned_longitude = pruneList(longitude)
        longitude = pruned_longitude
    
    print("Prune relativ alititude")
    for x in range(numberOfPrune):
        pruned_altitude = pruneList(relative_altitude)
        relative_altitude = pruned_altitude
    
    return latitude, longitude, relative_altitude

# ANIMATION FUNCTION: Helper function to viewRosbagWithRedDots()
def funcWithRedDots(num, dataSet, line, redDots):
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    redDots.set_data(dataSet[0:2, :num])    
    redDots.set_3d_properties(dataSet[2, :num]) 
    return line


    # Show the dataset in 3d, with a red dot for every datapoint 
def viewRosbagWithRedDots(latitude, longitude, relative_altitude):
    t = relative_altitude
    x = latitude
    y = longitude
    dataSet = np.array([x, y, t])
    numDataPoints = len(t)

    # GET SOME MATPLOTLIB OBJECTS
    fig = plt.figure()
    ax = Axes3D(fig)
    redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='r', marker='o')[0] # For scatter plot
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot

    # AXES PROPERTIES
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Relative altitude')
    ax.set_title('Drone flight')

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, funcWithRedDots, frames=numDataPoints, fargs=(dataSet,line,redDots), interval=50, blit=False)
 
    plt.show()


    # ANIMATION FUNCTION: Helper function to viewDataSetWithOutRedDot()
def funcWithOutRedDots(num, dataSet, line):
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    return line

    # Show the dataset in 3d, without a red dot for every datapoint 
def viewDataSetWithOutRedDot(latitude, longitude, relative_altitude):
    t = relative_altitude
    x = latitude
    y = longitude
    dataSet = np.array([x, y, t])
    numDataPoints = len(t)

    # GET SOME MATPLOTLIB OBJECTS
    fig = plt.figure()
    ax = Axes3D(fig)
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot

    # AXES PROPERTIES
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Relative altitude')
    ax.set_title('Drone flight')

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, funcWithOutRedDots, frames=numDataPoints, fargs=(dataSet,line), interval=50, blit=False)

    plt.show()


    # First argument # Path ex: dataFiles/drone_2021-09-12-16-13-35.csv
    # Second argument # reds dots on = True, off = False
    # Thrid arguments # numberofpruning (to view 317 lines of rosdata takes 21 sec)

def ViewCVSFile (path: str, redDots: bool, NumberOfScaleDown: int): 
    latitude, longitude, relative_altitude = readCSVFileAndPrep(path)
    
    resLatitude, resLongitude, resRelative_altitude = pruneDataSet(latitude, longitude, relative_altitude, NumberOfScaleDown)

    if redDots:
        viewRosbagWithRedDots(resLatitude, resLongitude, resRelative_altitude)
    else:
        viewDataSetWithOutRedDot(resLatitude, resLongitude, resRelative_altitude)

# Counts the rows in the provide CSV file
def countRowsInCSV(path):

    df = pd.read_csv(path)

    return len(df.index)







