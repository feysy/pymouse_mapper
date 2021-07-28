from PyQt6.QtWidgets import QListWidgetItem
from evdev.device import InputDevice


class DeviceModel(QListWidgetItem):
    def __init__(self, name: str, device: InputDevice) -> None:
        super().__init__(name)
        self.name = name
        self.device = device

    def __str__(self) -> str:
        return self.name