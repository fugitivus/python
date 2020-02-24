#!/usr/bin/env Python3      
#pip3 install PySimpleGui typing
#sudo apt-get install python3-tk
#doc: https://pypi.org/project/PySimpleGUI/
#doc: https://pysimplegui.readthedocs.io/en/latest/cookbook/
#doc: https://pypi.org/project/PySimpleGUI/2.30.0/

import PySimpleGUI as sg



# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Do you have a small Penis?')],
			[sg.Multiline('Do you have a small Penis?', key='IN', enter_submits=False)],
            [sg.RealtimeButton('Yes'), sg.RealtimeButton('No')]]

# Create the Window
window = sg.Window('I´ve run out of ideas...', layout)

# Event Loop to process "events"
while True:             
    event, values = window.Read(timeout=200)
    old = values['IN']
    print (old)

    print("Event: ", event, " IN: ", values['IN'])

    if event in ('\r', 'special 16777220', 'special 16777221'):         # Check for ENTER key
        elem = window.FindElementWithFocus()
        if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:
            elem.Click()

    if event is None:
        break

window.Close()
