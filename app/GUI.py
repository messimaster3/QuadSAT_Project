# GUI.py

from typing import Sized
from typing_extensions import TypeGuard
import PySimpleGUI as sg
import main 

# view start view
startView=[
    [
        sg.Text("View RosBag"),
        sg.In (size =(25,1), enable_events=True, key="-FILE-"), 
        sg.FileBrowse(),
    ],
    [
        sg.Text("Place a red dot, for every datapoint viewed for the RosFile"),
        sg.CB("Red dots", key="-REDDOTS-")
    ],
    [
        sg.Text("Inter number of times the data should be pruned"),
        sg.In (enable_events= True, key ="-NUMBEROFPRUNE-")
    ],
    [
        sg.Text("Run program: "),
        sg.B("Run", enable_events=True, key="-RUN-")
    ],    
]


window = sg.Window("Drone flight view", startView)


#event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Runs the program when a user hits run
    if event == "-RUN-":
        try:
            # type str
            path = values["-FILE-"]
            # Check to see if the last 3 letters is cvs
            if path[-3:] != "csv":
                raise TypeError("The selected file is a not a cvs file")
            # type bool
            redDots = values['-REDDOTS-']
            # type int
            numberOfScaleDown = values["-NUMBEROFPRUNE-"]
            # Checks to see if the input is a number
            if not numberOfScaleDown.isdigit():
                raise TypeError("The number of scaledown must be a int")
            numberOfScaleDownInt = int(numberOfScaleDown)
            main.ViewCVSFile(path, redDots, numberOfScaleDownInt)
        except TypeError as error:
            print(error)

window.close()
