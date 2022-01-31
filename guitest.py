import PySimpleGUI as sg
from Controller import outputSign

sg.theme('Dark Blue 3')
layout = [[sg.Text("Welcome to Sign Language Interpreter")], [sg.Button("Audio to Sign")], [sg.Button("Dictionary")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Audio to Sign":
        outputSign.output_sign(1)

    elif event == sg.WIN_CLOSED:
        break

window.close()