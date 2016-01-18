from evdev import uinput, ecodes as e
import time


test = "es"

print("Aloitetaan viiden sekunnin päästä...")
time.sleep(5)

while test == "es":
	with uinput.UInput() as ui:
		ui.write(e.EV_KEY, e.KEY_F, 1)
		ui.write(e.EV_KEY, e.KEY_ENTER, 1)
		ui.syn()