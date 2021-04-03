# pymouse-mapper
A small script for mapping mouse buttons to keystrokes on Wayland.

It works by reading from `python-libinput` and triggering key events using `evemu`
depending on the recognized button from the recognized device.

Got a lot of ideas from here https://github.com/mathportillo/wayland-mouse-mapper

## Buttons
Currently only configured to work on wheel horizontal axis to change workspaces

## Prerequisites
The script depends on the following executables being available in your PATH:
- libinput
- evemu

to install those just run the following command (with root privileges):
```
sudo apt-get install libinput-tools evemu-tools
```

## Usage
Run the following command (with root privileges):
```
python3 pymouse_mapper.sh
```

## Installation (start at boot)
Run the following commands (with root privileges):

```
cp pymouse_mapper.py /usr/bin/
cp pymouse_mapper.service /usr/lib/systemd/system/
systemctl enable pymouse_mapper.service
systemctl start pymouse_mapper.service
```

##TODO
All can be done with a single library maybe
https://python-evdev.readthedocs.io/en/latest/tutorial.html#injecting-events-using-a-context-manager