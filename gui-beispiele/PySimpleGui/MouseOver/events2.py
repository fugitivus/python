# Testing async window, see if can have a slider
# that adjusts the size of text displayed

import PySimpleGUI as sg
fontSize = 12
layout = [[sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
           sg.Slider(range=(6,172), orientation='h', size=(10,20),
           change_submits=True, key='slider', font=('Helvetica 20')),
           sg.Text("Aa", size=(2, 1), font="Helvetica "  + str(fontSize), key='text')]]

sz = fontSize
window = sg.Window("Font size selector", layout, grab_anywhere=False)
# Event Loop
while True:
    event, values= window.Read()
    if event is None:
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])
    sz = sz_spin if sz_spin != fontSize else sz_slider
    if sz != fontSize:
        fontSize = sz
        font = "Helvetica "  + str(fontSize)
        window.FindElement('text').Update(font=font)
        window.FindElement('slider').Update(sz)
        window.FindElement('spin').Update(sz)

print("Done.")
