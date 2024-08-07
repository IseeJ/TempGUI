# -*- coding: utf-8 AA-*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QModelIndex, QObject, QPoint
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QImage, QIcon
from pyqtgraph import PlotWidget, GraphicsLayoutWidget
from PyQt5.QtWidgets import*

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.colors = [(183, 101, 224), (93, 131, 212), (49, 205, 222), (36, 214, 75), (214, 125, 36) ,(230, 78, 192), (209, 84, 65), (0, 184, 245)]
        #self.centralwidget = DiagramWidget(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.mainsetup_1 = QtWidgets.QHBoxLayout()
        self.mainsetup_1.setObjectName("setupLayout")
        
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.setText("Refresh Port")
        self.mainsetup_1.addWidget(self.refreshButton)

        self.intervalInput = QtWidgets.QLineEdit(self.centralwidget)
        self.intervalInput.setObjectName("intervalInput")
        self.intervalInput.setPlaceholderText("Logging Interval (s)")
        self.intervalInput.setMaximumSize(QtCore.QSize(200, 16777215)) 
        self.mainsetup_1.addWidget(self.intervalInput)
        
        self.LogBothButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogBothButton.setObjectName("LogBothButton")
        self.LogBothButton.setText("Log Both")
        self.LogBothButton.setMaximumSize(QtCore.QSize(200, 16777215)) 
        self.mainsetup_1.addWidget(self.LogBothButton)

        self.startStopButton = QtWidgets.QPushButton(self.centralwidget)
        self.startStopButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.startStopButton.setObjectName("startStopButton")
        self.mainsetup_1.addWidget(self.startStopButton)

        self.verticalLayout.addLayout(self.mainsetup_1)

        
        #HUMIDITY
        #sub Hum 1
        self.HumHLayout_1 = QtWidgets.QHBoxLayout()
        self.HumHLayout_1.setObjectName("HumHLayout")
        
        self.HumPortBox = QtWidgets.QComboBox(self.centralwidget)
        self.HumPortBox.setObjectName("HumPortBox")
        self.HumHLayout_1.addWidget(self.HumPortBox)
        
        self.HumBaudBox = QtWidgets.QComboBox(self.centralwidget)
        self.HumBaudBox.setObjectName("HumBaudBox")
        self.HumBaudBox.addItems(["9600", "4800", "9600","19200", "38400", "57600", "115200"])
        self.HumHLayout_1.addWidget(self.HumBaudBox)

        self.HumsaveDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumsaveDirectoryButton.setObjectName("HumsaveDirectoryButton")
        self.HumsaveDirectoryButton.setText("File Directory")
        self.HumHLayout_1.addWidget(self.HumsaveDirectoryButton)


        """
        self.HumrefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumrefreshButton.setObjectName("HumrefreshButton")
        self.HumrefreshButton.setText("Refresh")
        self.HumHLayout_1.addWidget(self.HumrefreshButton)
 
        self.HumIntInput = QtWidgets.QLineEdit(self.centralwidget)
        self.HumIntInput.setObjectName("HumIntInput")
        self.HumIntInput.setPlaceholderText("Logging Interval (s)")
        self.HumIntInput.setMaximumSize(QtCore.QSize(200, 16777215))
        self.HumHLayout_1.addWidget(self.HumIntInput)
        """
        self.HumLogButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumLogButton.setObjectName("HumLogButton")
        self.HumLogButton.setText("Log Humudity")
        self.HumHLayout_1.addWidget(self.HumLogButton)
        
        self.HumfileLabel = QtWidgets.QLabel(self.centralwidget)
        self.HumfileLabel.setObjectName("HumfileLabel")
        self.HumHLayout_1.addWidget(self.HumfileLabel)
        
        self.verticalLayout.addLayout(self.HumHLayout_1)


        #sub Hum 2
        self.HumHLayout_2 = QtWidgets.QHBoxLayout()
        self.HumHLayout_2.setObjectName("HumHLayout_2")

        self.HumVLayout_2_1 = QtWidgets.QVBoxLayout()
        self.HumVLayout_2_1.setObjectName("HumVLayout_2_1")
        self.HumHLayout_2.addLayout(self.HumVLayout_2_1)

        self.Humlabel1 = QtWidgets.QLabel(self.centralwidget)
        self.Humlabel1.setObjectName("Humlabel2")
        self.Humlabel1.setText(f"RH: --")
        self.Humlabel1.setStyleSheet(f"font-weight: bold; font-size: 14px; color: rgb(190, 17, 17); background-color: white; border: 1px solid black;")
        self.Humlabel1.setFixedSize(100, 40)
        self.HumVLayout_2_1.addWidget(self.Humlabel1)

        self.Humlabel2 = QtWidgets.QLabel(self.centralwidget)
        self.Humlabel2.setObjectName("Humlabel2")
        self.Humlabel2.setText(f"Tmp: --")
        self.Humlabel2.setStyleSheet(f"font-weight: bold; font-size: 14px; color: rgb(0, 184, 245) ; background-color: white; border: 1px solid black;")
        self.Humlabel2.setFixedSize(100, 40)
        self.HumVLayout_2_1.addWidget(self.Humlabel2)

        self.Humlabel3 = QtWidgets.QLabel(self.centralwidget)
        self.Humlabel3.setObjectName("Humlabel2")
        self.Humlabel3.setText(f"Dew: --")
        self.Humlabel3.setStyleSheet(f"font-weight: bold; font-size: 14px; color: black ; background-color: white; border: 1px solid black;")
        self.Humlabel3.setFixedSize(100, 40)
        self.HumVLayout_2_1.addWidget(self.Humlabel3)

        self.HumclearButton = QtWidgets.QPushButton(self.centralwidget)
        self.HumclearButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.HumclearButton.setObjectName("HumclearButton")
        self.HumclearButton.setText("Clear")
        self.HumVLayout_2_1.addWidget(self.HumclearButton)
        

        self.graphics_layout = GraphicsLayoutWidget(self.centralwidget)
        self.graphics_layout.setMinimumSize(QtCore.QSize(400,300))
        self.HumHLayout_2.addWidget(self.graphics_layout)

        """
        self.HumPlotWidget = PlotWidget(self.centralwidget)
        self.HumPlotWidget.setMinimumSize(QtCore.QSize(348,305))
        self.HumPlotWidget.setObjectName("HumPlotWidget")
        self.HumHLayout_2.addWidget(self.HumPlotWidget)
        """
        self.HumPlotWidget2 = PlotWidget(self.centralwidget)
        self.HumPlotWidget2.setMinimumSize(QtCore.QSize(400,300))
        self.HumPlotWidget2.setObjectName("HumPlotWidget2")
        self.HumHLayout_2.addWidget(self.HumPlotWidget2)
        
        
        self.verticalLayout.addLayout(self.HumHLayout_2)

        
        
        #for temperature
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #Port
        self.TempPortBox = QtWidgets.QComboBox(self.centralwidget)
        self.TempPortBox.setObjectName("TempPortBox")
        self.horizontalLayout_2.addWidget(self.TempPortBox)
        #baud
        self.TempBaudBox = QtWidgets.QComboBox(self.centralwidget)
        self.TempBaudBox.setObjectName("TempBaudBox")
        self.TempBaudBox.addItems(["38400", "4800", "9600","19200", "57600", "115200"])
        self.horizontalLayout_2.addWidget(self.TempBaudBox)




        """
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setObjectName("ConnectButton")
        self.ConnectButton.setText("Connect")
        self.horizontalLayout_2.addWidget(self.ConnectButton)
        """
        
        self.saveDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDirectoryButton.setObjectName("saveDirectoryButton")
        self.saveDirectoryButton.setText("File Directory")
        self.horizontalLayout_2.addWidget(self.saveDirectoryButton)

        self.TempLogButton = QtWidgets.QPushButton(self.centralwidget)
        self.TempLogButton.setObjectName("TempLogButton")
        self.TempLogButton.setText("Log Temperature")
        self.horizontalLayout_2.addWidget(self.TempLogButton)
        #self.TempLogButton.setMaximumSize(QtCore.QSize(100, 16777215))
        
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setObjectName("fileLabel")
        #self.fileLabel.setMaximumSize(QtCore.QSize(100, 500))
        self.horizontalLayout_2.addWidget(self.fileLabel)

        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        #to contain diagram and labels
        height = 560
        width = int(height/2.3)
        self.DiagramWidget = QtWidgets.QWidget(self.centralwidget)
        self.DiagramWidget.setFixedSize(width, height)
        self.DiagramLayout = QtWidgets.QStackedLayout(self.DiagramWidget)

        self.imageLabel = QtWidgets.QLabel()
        pixmap = QPixmap("diagram.png")
        pixmap = pixmap.scaled(width, height)
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setGeometry(0, 0, width, height)

        self.DiagramLayout.addWidget(self.imageLabel)
        self.labels = []
        for i in range(8):
            label = QtWidgets.QLabel(self.DiagramWidget)
            label.setText(f"T{i+1}")
            label.setStyleSheet(f"font-weight: bold; font-size: 14px; color: white ; background-color: rgb{self.colors[i]}; border: 1px solid black;")
            label.setFixedSize(70, 30)
            #label.move(i*20, i*20)
            self.labels.append(label)
            
        self.labels[0].move(int(0.02*width),int(0.88*height))  #T1
        self.labels[1].move(int(0.14*width),int(0.80*height))  #T2
        self.labels[2].move(int(0.24*width),int(0.71*height))  #T3
        self.labels[3].move(int(0.64*width),int(0.55*height)) #T4
        self.labels[4].move(int(0.20*width),int(0.46*height))  #T5
        self.labels[5].move(int(0.66*width),int(0.41*height)) #T6
        self.labels[6].move(int(0.64*width),int(0.28*height)) #T7
        self.labels[7].move(int(0.26*width),int(0.1*height))   #T8
        self.horizontalLayout.addWidget(self.DiagramWidget)

        """
        spacerWidth = 300
        spacerItem = QtWidgets.QSpacerItem(spacerWidth, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        """                             
                       
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setMinimumSize(QtCore.QSize(348, 0))
        self.graphWidget.setObjectName("PlotWidget") 
        self.horizontalLayout.addWidget(self.graphWidget)        
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkboxes = []
        for i in range(8):
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setMaximumSize(QtCore.QSize(60,30))
            self.checkBox.setMinimumSize(QtCore.QSize(40,0))
            self.checkBox.setObjectName(f"T{i+1}")
            self.checkBox.setChecked(True)
            self.verticalLayout_2.addWidget(self.checkBox)
            self.checkBox.setStyleSheet(f"font-weight: bold; font-size: 14px; color: white; background-color: rgb{self.colors[i]}; border: 1px solid black;")
            self.checkboxes.append(self.checkBox)

        
        #still buggy
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setText("Clear")
        self.verticalLayout_2.addWidget(self.clearButton)


        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        """
        #import
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.menuFile.addAction(self.actionImport)
        self.menubar.addAction(self.menuFile.menuAction())
        """
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature and Humidity Monitor"))

        for i in range(8):
            self.checkboxes[i].setText(_translate("MainWindow",f"T{i+1}"))
            self.labels[i].setText(_translate("MainWindow", f"T{i+1}"))

        self.startStopButton.setText(_translate("MainWindow", "Start/Stop"))
        #self.clearButton.setText(_translate("MainWindow", "Clear"))
    
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        #self.actionImport.setText(_translate("MainWindow", "Import"))

if __name__ == "__main__":
    import sys, os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
