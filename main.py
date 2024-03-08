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
BUTTON_SIZE = (4,2)
DISPLAY_WIDTH = 14
DISPLAY_HEIGHT = 3
DISPLAY_KEY = "DISPLAY"

BLACK = "black"
WHITE = "white"
DARK_GRAY = "darkgray"
WHITE_ON_RED = "white on red"
BLACK_ON_LIGHT_GRAY = "black on lightgray"
BLACK_ON_LIGHT_BLUE = "black on lightblue"

#   FUNCTIONS
def create_button(label, color=BLACK_ON_LIGHT_GRAY):
    button = sg.Button(label, size=BUTTON_SIZE, button_color=color)
    return button

#   GLOBAL VARIABLES
display = sg.Text("",
                  key=DISPLAY_KEY,
                  size=(DISPLAY_WIDTH, DISPLAY_HEIGHT),
                  relief=sg.RELIEF_SUNKEN,
                  border_width=1,
                  justification="right",
                  font=("sans-serif", 12),
                  expand_x=True,
                  text_color=BLACK,
                  background_color=WHITE)

layout = [
    [ create_button("C", WHITE_ON_RED), display ],
    [ create_button("7"), create_button("8"), create_button("9"), create_button("+", BLACK_ON_LIGHT_BLUE) ],
    [ create_button("4"), create_button("5"), create_button("6"), create_button("-", BLACK_ON_LIGHT_BLUE) ],
    [ create_button("1"), create_button("2"), create_button("3"), create_button("x", BLACK_ON_LIGHT_BLUE) ],
    [ create_button("."), create_button("0"), create_button("=", BLACK_ON_LIGHT_BLUE), create_button("/", BLACK_ON_LIGHT_BLUE) ]
]

window = sg.Window("Calculator", layout, background_color=DARK_GRAY)

#   MAIN PROGRAM
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
