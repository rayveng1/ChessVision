from pathlib import Path
import PySimpleGUI as sg
import subprocess
import sys
import Board_Digitizer_Roboflow as script
import os


sg.theme("DarkBlue")

layout = [
    [sg.Text('Evaluation Image'), sg.InputText(
        key='-file1-'), sg.FileBrowse()],
    [sg.Button("Go")],
]

window = sg.Window('ChessVision', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Go":
        filepath = values['-file1-']
        while True:
            if not Path(filepath).is_file():
                if filepath == '':
                    sg.popup_ok('Select a file for evaluation!')
                else:
                    sg.popup_ok('File is invalid!')
                filepath = sg.popup_get_file("", no_window=True)
                if filepath == '':
                    break
                window['-file1-'].update(filepath)
            else:
                # print(filepath)
                script.resizer(filepath)
                script.imageSplitter()
                print(script.infrencing())
                break

window.close()
