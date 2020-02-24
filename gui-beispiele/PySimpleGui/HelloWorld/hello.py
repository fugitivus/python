#!/usr/bin/env Python3      
#pip3 install PySimpleGui typing
#sudo apt-get install python3-tk
#doc: https://pypi.org/project/PySimpleGUI/
#doc: https://pysimplegui.readthedocs.io/en/latest/cookbook/
#doc: https://pypi.org/project/PySimpleGUI/2.30.0/

import PySimpleGUI as sg
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Hello World', font='Courier 12', text_color='blue', background_color='green')],
            [sg.Text('Enter something'), sg.InputText()],
            [sg.Text('File:'), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('HelloWorld in Python3', layout)
# Event Loop to process "events"
while True:             
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break

window.Close()
