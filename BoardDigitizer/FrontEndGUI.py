from pathlib import Path
import PySimpleGUI as sg
import subprocess
import sys
import Board_Digitizer_Roboflow as script
import os

if os.path.exists("/Users/connorscally/Documents/GitHub/ChessVision/BoardDigitizer/chessboard_splits/.DS_Store"):
    os.remove("/Users/connorscally/Documents/GitHub/ChessVision/BoardDigitizer/chessboard_splits/.DS_Store")

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
                script.resizer(filepath)
                script.imageSplitter()
                FEN = script.fenConversion(script.infrencing())
                script.chess(FEN)
                script.evaluation()
                break

window.close()
