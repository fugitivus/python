import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

text_elem = sg.Text("", size=(18, 1))

layout = [[sg.Text("Press a key or scroll mouse")],
			[text_elem],
			[sg.Button("OK")]]

window = sg.Window("Keyboard Test", layout, return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
	event, value = window.Read()

	if event == "OK" or event is None:
		print(event, "exiting")
		break

	print("Event: ",event," Value: ",value)

	if event == {} and value == {}:
		print("Enter Key was Pressed....")



text_elem.Update(event)
