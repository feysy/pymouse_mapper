# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designercvSxat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.left_panel = QVBoxLayout()
        self.left_panel.setObjectName(u"left_panel")
        self.list_device = QListWidget(self.centralwidget)
        self.list_device.setObjectName(u"list_device")
        self.list_device.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.list_device.sizePolicy().hasHeightForWidth())
        self.list_device.setSizePolicy(sizePolicy)
        self.list_device.setAutoFillBackground(False)
        self.list_device.setResizeMode(QListView.Adjust)
        self.list_device.setLayoutMode(QListView.SinglePass)

        self.left_panel.addWidget(self.list_device)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.left_panel.addWidget(self.btn_refresh)


        self.main_layout.addLayout(self.left_panel)

        self.right_panel = QVBoxLayout()
        self.right_panel.setObjectName(u"right_panel")
        self.info_text = QTextEdit(self.centralwidget)
        self.info_text.setObjectName(u"info_text")

        self.right_panel.addWidget(self.info_text)


        self.main_layout.addLayout(self.right_panel)


        self.horizontalLayout_2.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

