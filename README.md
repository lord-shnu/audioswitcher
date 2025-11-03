# audioswitcher
MacOS Audio Switcher for programs such as Logic X, Ableton Live, etc. to instantly reset coreaudiod with a single click. <br>
**BROKEN AS OF 11/2/2025, WORKING ON FIX, PYTHON BEHAVING ODD ON M SERIES**


Workaround: <br>
Create new Automator App. <br>
Choose "Run Shell Script" <br>
Shell: /bin/bash  |  Pass input: to stdin

Paste into box:

**export SUDO_ASKPASS="/usr/local/bin/askpass_gui.sh" <br>
/usr/bin/sudo -A /usr/bin/killall coreaudiod** <br>

Save it, name whatever you want. Use spotlight/raycast/alfred/launchpad(r.i.p.) to launch whenever you need to reset coreaudiod. (requires password on every restart)
