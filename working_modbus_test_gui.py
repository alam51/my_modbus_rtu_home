# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modbus_gui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1773, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 241, 303))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_Bay_1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_Bay_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Bay_1.setObjectName("gridLayout_Bay_1")
        self.label_I1_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I1_1.setFont(font)
        self.label_I1_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I1_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I1_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I1_1.setObjectName("label_I1_1")
        self.gridLayout_Bay_1.addWidget(self.label_I1_1, 2, 0, 1, 1)
        self.label_I2_Val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I2_Val_1.setFont(font)
        self.label_I2_Val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I2_Val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I2_Val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I2_Val_1.setObjectName("label_I2_Val_1")
        self.gridLayout_Bay_1.addWidget(self.label_I2_Val_1, 3, 1, 1, 1)
        self.label_P_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_P_1.setFont(font)
        self.label_P_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_P_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_P_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_P_1.setObjectName("label_P_1")
        self.gridLayout_Bay_1.addWidget(self.label_P_1, 5, 0, 1, 1)
        self.label_Q_val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Q_val_1.setFont(font)
        self.label_Q_val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q_val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Q_val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Q_val_1.setObjectName("label_Q_val_1")
        self.gridLayout_Bay_1.addWidget(self.label_Q_val_1, 6, 1, 1, 1)
        self.label_I3_Val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I3_Val_1.setFont(font)
        self.label_I3_Val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I3_Val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I3_Val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I3_Val_1.setObjectName("label_I3_Val_1")
        self.gridLayout_Bay_1.addWidget(self.label_I3_Val_1, 4, 1, 1, 1)
        self.label_Voltage_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Voltage_1.setFont(font)
        self.label_Voltage_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Voltage_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Voltage_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Voltage_1.setObjectName("label_Voltage_1")
        self.gridLayout_Bay_1.addWidget(self.label_Voltage_1, 1, 0, 1, 1)
        self.label_Voltage_Val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_Voltage_Val_1.setFont(font)
        self.label_Voltage_Val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Voltage_Val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Voltage_Val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Voltage_Val_1.setObjectName("label_Voltage_Val_1")
        self.gridLayout_Bay_1.addWidget(self.label_Voltage_Val_1, 1, 1, 1, 1)
        self.label_I3_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I3_1.setFont(font)
        self.label_I3_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I3_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I3_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I3_1.setObjectName("label_I3_1")
        self.gridLayout_Bay_1.addWidget(self.label_I3_1, 4, 0, 1, 1)
        self.label_P_Val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_P_Val_1.setFont(font)
        self.label_P_Val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_P_Val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_P_Val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_P_Val_1.setObjectName("label_P_Val_1")
        self.gridLayout_Bay_1.addWidget(self.label_P_Val_1, 5, 1, 1, 1)
        self.label_I2_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I2_1.setFont(font)
        self.label_I2_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I2_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I2_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I2_1.setObjectName("label_I2_1")
        self.gridLayout_Bay_1.addWidget(self.label_I2_1, 3, 0, 1, 1)
        self.label_I1_Val_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I1_Val_1.setFont(font)
        self.label_I1_Val_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I1_Val_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I1_Val_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I1_Val_1.setObjectName("label_I1_Val_1")
        self.gridLayout_Bay_1.addWidget(self.label_I1_Val_1, 2, 1, 1, 1)
        self.label_Q_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Q_1.setFont(font)
        self.label_Q_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Q_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Q_1.setObjectName("label_Q_1")
        self.gridLayout_Bay_1.addWidget(self.label_Q_1, 6, 0, 1, 1)
        self.label_Bay_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Bay_1.setFont(font)
        self.label_Bay_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Bay_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Bay_1.setObjectName("label_Bay_1")
        self.gridLayout_Bay_1.addWidget(self.label_Bay_1, 0, 0, 1, 2)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(310, 50, 241, 303))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_Bay_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_Bay_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Bay_2.setObjectName("gridLayout_Bay_2")
        self.label_I1_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I1_2.setFont(font)
        self.label_I1_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I1_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I1_2.setObjectName("label_I1_2")
        self.gridLayout_Bay_2.addWidget(self.label_I1_2, 2, 0, 1, 1)
        self.label_I2_Val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I2_Val_2.setFont(font)
        self.label_I2_Val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I2_Val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I2_Val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I2_Val_2.setObjectName("label_I2_Val_2")
        self.gridLayout_Bay_2.addWidget(self.label_I2_Val_2, 3, 1, 1, 1)
        self.label_P_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_P_2.setFont(font)
        self.label_P_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_P_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_P_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_P_2.setObjectName("label_P_2")
        self.gridLayout_Bay_2.addWidget(self.label_P_2, 5, 0, 1, 1)
        self.label_Q_val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Q_val_2.setFont(font)
        self.label_Q_val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q_val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Q_val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Q_val_2.setObjectName("label_Q_val_2")
        self.gridLayout_Bay_2.addWidget(self.label_Q_val_2, 6, 1, 1, 1)
        self.label_I3_Val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I3_Val_2.setFont(font)
        self.label_I3_Val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I3_Val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I3_Val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I3_Val_2.setObjectName("label_I3_Val_2")
        self.gridLayout_Bay_2.addWidget(self.label_I3_Val_2, 4, 1, 1, 1)
        self.label_Voltage_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Voltage_2.setFont(font)
        self.label_Voltage_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Voltage_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Voltage_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Voltage_2.setObjectName("label_Voltage_2")
        self.gridLayout_Bay_2.addWidget(self.label_Voltage_2, 1, 0, 1, 1)
        self.label_Voltage_Val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Voltage_Val_2.setFont(font)
        self.label_Voltage_Val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Voltage_Val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Voltage_Val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Voltage_Val_2.setObjectName("label_Voltage_Val_2")
        self.gridLayout_Bay_2.addWidget(self.label_Voltage_Val_2, 1, 1, 1, 1)
        self.label_I3_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I3_2.setFont(font)
        self.label_I3_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I3_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I3_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I3_2.setObjectName("label_I3_2")
        self.gridLayout_Bay_2.addWidget(self.label_I3_2, 4, 0, 1, 1)
        self.label_P_Val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_P_Val_2.setFont(font)
        self.label_P_Val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_P_Val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_P_Val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_P_Val_2.setObjectName("label_P_Val_2")
        self.gridLayout_Bay_2.addWidget(self.label_P_Val_2, 5, 1, 1, 1)
        self.label_I2_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_I2_2.setFont(font)
        self.label_I2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_I2_2.setObjectName("label_I2_2")
        self.gridLayout_Bay_2.addWidget(self.label_I2_2, 3, 0, 1, 1)
        self.label_I1_Val_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_I1_Val_2.setFont(font)
        self.label_I1_Val_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_I1_Val_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_I1_Val_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_I1_Val_2.setObjectName("label_I1_Val_2")
        self.gridLayout_Bay_2.addWidget(self.label_I1_Val_2, 2, 1, 1, 1)
        self.label_Q_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Q_2.setFont(font)
        self.label_Q_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Q_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Q_2.setObjectName("label_Q_2")
        self.gridLayout_Bay_2.addWidget(self.label_Q_2, 6, 0, 1, 1)
        self.label_Bay_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Bay_2.setFont(font)
        self.label_Bay_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Bay_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Bay_2.setObjectName("label_Bay_2")
        self.gridLayout_Bay_2.addWidget(self.label_Bay_2, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1773, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pymodbus Gui Test"))
        self.label_I1_1.setText(_translate("MainWindow", "I1(A)"))
        self.label_I2_Val_1.setText(_translate("MainWindow", "0"))
        self.label_P_1.setText(_translate("MainWindow", "P(MW)"))
        self.label_Q_val_1.setText(_translate("MainWindow", "0"))
        self.label_I3_Val_1.setText(_translate("MainWindow", "0"))
        self.label_Voltage_1.setText(_translate("MainWindow", "Voltage(kV)"))
        self.label_Voltage_Val_1.setText(_translate("MainWindow", "0"))
        self.label_I3_1.setText(_translate("MainWindow", "I3(A)"))
        self.label_P_Val_1.setText(_translate("MainWindow", "0"))
        self.label_I2_1.setText(_translate("MainWindow", "I2(A)"))
        self.label_I1_Val_1.setText(_translate("MainWindow", "0"))
        self.label_Q_1.setText(_translate("MainWindow", "Q(MVAR)"))
        self.label_Bay_1.setText(_translate("MainWindow", "Bay1"))
        self.label_I1_2.setText(_translate("MainWindow", "I1(A)"))
        self.label_I2_Val_2.setText(_translate("MainWindow", "0"))
        self.label_P_2.setText(_translate("MainWindow", "P(MW)"))
        self.label_Q_val_2.setText(_translate("MainWindow", "0"))
        self.label_I3_Val_2.setText(_translate("MainWindow", "0"))
        self.label_Voltage_2.setText(_translate("MainWindow", "Voltage(kV)"))
        self.label_Voltage_Val_2.setText(_translate("MainWindow", "0"))
        self.label_I3_2.setText(_translate("MainWindow", "I3(A)"))
        self.label_P_Val_2.setText(_translate("MainWindow", "0"))
        self.label_I2_2.setText(_translate("MainWindow", "I2(A)"))
        self.label_I1_Val_2.setText(_translate("MainWindow", "0"))
        self.label_Q_2.setText(_translate("MainWindow", "Q(MVAR)"))
        self.label_Bay_2.setText(_translate("MainWindow", "Bay1"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_data)
        timer.start(300)  # mili second
        self.update_data()

    def update_data(self):
        _translate = QtCore.QCoreApplication.translate
        # time_str = QTime.currentTime().toString()
        time_str = datetime.datetime.now()
        val = str(datetime.datetime.now())
        a = self.label_Voltage_Val_1
        # self.label_Voltage_Val_1.setText(_translate("MainWindow", val))
        a.setText(_translate("MainWindow", val))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())