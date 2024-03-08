#
#   Calculator - PySimpleGUI
#
#   A simple four-function calculator in Python using the PySimpleGUI library
#
#   Author: Robert Walsh
#   Date:   March 8, 2024
#

#   IMPORTS
import PySimpleGUI as sg

#   CONSTANTS

#   FUNCTIONS
def create_button(label):
    button = sg.Button(label)
    return button

#   GLOBAL VARIABLES
layout = [
    [ create_button("C"), sg.Text("-123456789.0") ],
    [ create_button("7"), create_button("8"), create_button("9"), create_button("+") ],
    [ create_button("4"), create_button("5"), create_button("6"), create_button("-") ],
    [ create_button("1"), create_button("2"), create_button("3"), create_button("x") ],
    [ create_button("."), create_button("0"), create_button("="), create_button("/") ]
]

window = sg.Window("Calculator", layout)

#   MAIN PROGRAM
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
