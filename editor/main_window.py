# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from typing import Optional
from PyQt6 import QtCore, QtWidgets
import evdev
from editor.model import DeviceModel

EV_KEY = 1
BTN_MOUSE = 272

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(813, 546)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.left_panel = QtWidgets.QVBoxLayout()
        self.left_panel.setObjectName("left_panel")
        self.list_device = QtWidgets.QListWidget(self.centralwidget)
        self.list_device.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_device.sizePolicy().hasHeightForWidth())
        self.list_device.setSizePolicy(sizePolicy)
        self.list_device.setAutoFillBackground(False)
        self.list_device.setResizeMode(QtWidgets.QListView.ResizeMode.Adjust)
        self.list_device.setLayoutMode(QtWidgets.QListView.LayoutMode.SinglePass)
        self.list_device.setObjectName("list_device")
        self.left_panel.addWidget(self.list_device)
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName("btn_refresh")
        self.left_panel.addWidget(self.btn_refresh)
        self.main_layout.addLayout(self.left_panel)
        self.right_panel = QtWidgets.QVBoxLayout()
        self.right_panel.setObjectName("right_panel")
        self.info_text = QtWidgets.QTextEdit(self.centralwidget)
        self.info_text.setObjectName("info_text")
        self.right_panel.addWidget(self.info_text)
        self.main_layout.addLayout(self.right_panel)
        self.horizontalLayout_2.addLayout(self.main_layout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 20))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_refresh.clicked.connect(self.refresh_devices)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_refresh.setText(_translate("MainWindow", "Refresh Devices"))

    def refresh_devices(self):
        self.list_device.clear()
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            capabilities = device.capabilities() # 272
            if EV_KEY in capabilities.keys():
                if BTN_MOUSE in capabilities[EV_KEY]:
                    self.list_device.insertItem(self.list_device.count(), DeviceModel(device.name, device.path))

