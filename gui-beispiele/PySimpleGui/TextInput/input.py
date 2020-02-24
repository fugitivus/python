#!/usr/bin/env Python3      
#pip3 install PySimpleGui typing
#sudo apt-get install python3-tk
#doc: https://pypi.org/project/PySimpleGUI/
#doc: https://pysimplegui.readthedocs.io/en/latest/cookbook/
#doc: https://pypi.org/project/PySimpleGUI/2.30.0/

import PySimpleGUI as sg      

layout = [[sg.Text('Persistent window',key='out')], 
          [sg.Input(key='in')],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:      
    event, values = window.Read() 
    print(event, values) 
          
    if event is None or event == 'Exit':
        break
	
    if event == 'Read':
        # Update the "output" text element to be the value of "input" element
        print("Show was pressed...")
        window['out'].Update(values['in'])

window.Close()
