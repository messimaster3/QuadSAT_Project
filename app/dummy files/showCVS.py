import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

def pruneList(listToPrune):
    return np.delete(listToPrune, np.arange(0, listToPrune.size, 2))


latitude = []
longitude = []
relative_altitude = []

data = pd.read_csv("drone_2021-09-12-16-13-35.csv")

latitude = np.concatenate((data[['field.latitude']].to_numpy()), axis=None)    
longitude = np.concatenate((data[['field.longitude']].to_numpy()), axis=None)
relative_altitude = np.concatenate((data[['field.relative_altitude']].to_numpy()), axis=None)

print("Prune latitude")
for x in range(7):
    pruned_latitude = pruneList(latitude)
    latitude = pruned_latitude
    print("Number " + str(x) + "  " + str(len(latitude)))

print("Prune longitude")
for x in range(7):
    pruned_longitude = pruneList(longitude)
    longitude = pruned_longitude
    print("Number " + str(x) + "  " + str(len(longitude)))

print("relativ alititude")
for x in range(7):
    pruned_altitude = pruneList(relative_altitude)
    relative_altitude = pruned_altitude
    print("Number " + str(x) + "  " + str(len(relative_altitude)))

#print("latitude length " + str(len(latitude)))
#print("longitude length " + str(len(longitude)))
#print("relavtive altitude length " + str(len(relative_altitude)))

# ANIMATION FUNCTION
def func(num, dataSet, line, redDots):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    redDots.set_data(dataSet[0:2, :num])    
    redDots.set_3d_properties(dataSet[2, :num]) 
    return line
  
# THE DATA POINTS
t = relative_altitude
x = latitude
y = longitude
dataSet = np.array([x, y, t])
numDataPoints = len(t)
 
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = Axes3D(fig)
redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='r', marker='o')[0] # For scatter plot
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot
 
# AXES PROPERTIES]
# ax.set_xlim3d([limit0, limit1])
ax.set_xlabel('Latitude')
ax.set_ylabel('Longtude')
ax.set_zlabel('Relative altitude')
ax.set_title('Drone flight')
 
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line,redDots), interval=50, blit=False)
#line_ani.save(r'Animation.mp4')
  
plt.show()