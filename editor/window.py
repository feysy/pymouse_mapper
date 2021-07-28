from editor.model import DeviceModel
from tkinter import Button, Frame, Listbox, Menu
from tkinter.constants import BOTH, LEFT, RAISED, RIGHT, W, X, Y, YES
from tkinter import messagebox
import evdev

EV_KEY = 1
BTN_MOUSE = 272

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Item")
        file_menu.add_command(label="Exit", command=self.exit_program)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=edit_menu)

        left_frame = Frame(self, relief=RAISED, borderwidth=1, width=150)
        left_frame.pack(side=LEFT, fill=Y, expand=False, anchor=W)

        device_list = Listbox(left_frame)
        device_list.pack(fill=Y ,expand=True)
        device_list.bind('<<ListboxSelect>>', self.change_device_selection)
        self.device_list = device_list
        
        exit_button = Button(left_frame, text="Exit", command=self.exit_program)
        exit_button.pack(fill=X, side=RIGHT,expand=True,  padx=3, pady=3)
        
        refresh_devices = Button(left_frame, text="Refresh", command=self.refresh_devices)
        refresh_devices.pack(fill=X, side=LEFT,expand=True,  padx=3, pady=3)

        right_frame = Frame(self, relief=RAISED, borderwidth=1)
        right_frame.pack(fill=BOTH, expand=YES)

        exit_button2 = Button(right_frame, text="Exit", command=self.exit_program)
        exit_button2.pack(fill=X, side=RIGHT,expand=True,  padx=3, pady=3)

    def exit_program(self):
        exit()

    def refresh_devices(self):
        self.device_list.delete(0,len(self.device_list.keys()) - 1)
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            capabilities = device.capabilities() # 272
            if EV_KEY in capabilities.keys():
                if BTN_MOUSE in capabilities[EV_KEY]:
                    self.device_list.insert(len(self.device_list.keys()), DeviceModel(device.name, device.path))
                
    def change_device_selection(self, event):
        device = self.device_list.curselection()
        messagebox.showinfo(device.name)