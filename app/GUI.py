# GUI.py

import PySimpleGUI as sg
import main 

# view start view
startView=[
    [
        sg.Text("View CSV file"),
        sg.In (size =(25,1), key="-FILE-"), 
        sg.FileBrowse(),
    ],
    [
        sg.Text("Place a red dot, for every data point viewed in the CSV file"),
        sg.CB("Red dots", key="-REDDOTS-")
    ],
    [
        sg.Text("Enter the number of times the data should be pruned"),
        sg.In (key ="-NUMBEROFPRUNE-")
    ],
    [
        sg.Text("Estimate the time the play back will take in minutes, with the current prune number"),
        sg.B("Check",enable_events=True, key="-CHECKTIME-"),
        sg.Text(key ="-OUTPUT-")
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
    elif event == "-CHECKTIME-":
        try:
            path = values["-FILE-"]
            # Check to see if the last 3 letters is cvs
            if path[-3:] != "csv":
                raise TypeError("The selected file is a not a cvs file")
            numberOfRows = main.countRowsInCSV(path)
            numberOfScaleDown = values["-NUMBEROFPRUNE-"]
            # Checks to see if the input is a number
            if not numberOfScaleDown.isdigit():
                raise TypeError("The number of scaledown must be a int")
            numberOfScaleDownInt = int(numberOfScaleDown)
            rowsAfterPrune = numberOfRows * 0.5 ** numberOfScaleDownInt
            # Takes 21 seconds to show 317 rows of data
            # Around 15 rows pr. second
            playBackTime = (rowsAfterPrune / 15) / 60
            window["-OUTPUT-"].update(playBackTime)
        except TypeError as error:
            print(error)

window.close()
