from libinput import LibInput, Event
from libinput.constant import DeviceCapability, Event as EventType, PointerAxis, Led
import os
 
event_type='EV_KEY'
prev_screen=['KEY_LEFTMETA', 'KEY_PAGEUP']
next_screen=['KEY_LEFTMETA', 'KEY_PAGEDOWN']
keyboard = None



li = LibInput(True, False, False)
li.udev_assign_seat('seat0')
for event in li.get_event():
    if (not keyboard) and event.type == EventType.DEVICE_ADDED:
        device = event.get_device()
        if event.get_device().has_capability(DeviceCapability.KEYBOARD) and device.get_id_vendor() > 0:
            keyboard = device.get_sysname()
            print(device.get_sysname())
            print(device.get_name())
            print(device.has_capability(DeviceCapability.KEYBOARD))
    if event.type == EventType.POINTER_AXIS:
        pointer_event = event.get_pointer_event()
        if pointer_event.has_axis(PointerAxis.SCROLL_HORIZONTAL):
            value = pointer_event.get_axis_value(PointerAxis.SCROLL_HORIZONTAL)
            keys = prev_screen
            if value > 0:
                keys = next_screen
            for key in keys:
                print(f"evemu-event --sync /dev/input/{keyboard} --type {event_type} --code {key} --value 1")
                os.system(f"evemu-event --sync /dev/input/{keyboard} --type {event_type} --code {key} --value 1")
            for key in keys:
                print(f"evemu-event --sync /dev/input/{keyboard} --type {event_type} --code {key} --value 0")
                os.system(f"evemu-event --sync /dev/input/{keyboard} --type {event_type} --code {key} --value 0")