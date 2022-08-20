from datetime import datetime
import sys
import Debug.Debug as Debug
import Py.TimeManagement as TimeManagement
import Py.DatabaseManagement as DatabaseManagement

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtGui

#Class file for app
class Timer(QWidget):
    def __init__(self):
        super().__init__()
        
        #setup database
        self.database = DatabaseManagement.database()
        self.database.create_table()
        #Setting window config
        self.WIDTH = 500
        self.HEIGHT = 500
        self.XPOS = 100
        self.YPOS = 100
        self.TITLE = "Title"
        self.ICON = ""
        
        #Instance Variables
        self.buttonPress = False

        #Calls ui creation
        self.initUI()

    #All the window setup
    def setupApp(self):
        Debug.log("Setting Up Window")
        #linking style sheet
        
        self.resize(self.WIDTH,self.HEIGHT)
        self.move(self.XPOS,self.YPOS)
        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QtGui.QIcon(self.ICON))

    #Adding a layout and adding widgets
    def setupLayout(self):
        Debug.log("Creating layout and adding widgets")
        MasterLayout = QVBoxLayout()
        HboxLayout = QHBoxLayout()

        self.timeLabel = QLabel("00:00:00")
        self.timeLabel.setAlignment(Qt.AlignCenter)
        MasterLayout.addWidget(self.timeLabel)

        self.button = QPushButton("Start")
        HboxLayout.addWidget(self.button)

        self.buttonSave = QPushButton("Save")
        HboxLayout.addWidget(self.buttonSave)

        MasterLayout.addLayout(HboxLayout)

        self.setLayout(MasterLayout)

        #other widgets
        self.timer = QTimer()
        return self.timeLabel

    #dedicated method to add actions to the widgets
    def WidgetActions(self):
        self.button.clicked.connect(self.buttonPressed)
        self.buttonSave.clicked.connect(self.saveButtonPressed)
        self.timer.timeout.connect(self.updateLabel)

    #Calls all apropriate methods to build the UI
    def initUI(self):
        self.setupApp()
        timeLabel = self.setupLayout()
        self.WidgetActions()

    #Below are all the actions performed in the app
    #Controls the button
    def buttonPressed(self):
        Debug.log("Button Pressed")
        if (self.buttonPress == False):
            self.start = TimeManagement.start_time()
            self.buttonPress = True
            self.timer.start(100)
            self.button.setText("Stop")

        elif (self.buttonPress == True):
            end = TimeManagement.final_time()
            self.buttonPress = False

            finalTime = end - self.start
            
            self.timer.stop()
            self.timeLabel.setText(str(finalTime).split(".")[0])
            self.button.setText("Start")

            
    def updateLabel(self):
        current = TimeManagement.final_time()
        time = current - self.start
        self.timeLabel.setText(str(time).split(".")[0])

    def saveButtonPressed(self):
        self.database.insert_time("test", datetime.now(), self.timeLabel.text())


#Main method
if __name__ == "__main__":
    #loading the app as an object and calling the widgets
    app = QApplication(sys.argv)

    #start app setup
    main = Timer()

    with open('./style/StyleSheet.qss', 'r') as f:
        style = f.read()

    main.setStyleSheet(style)
    
    main.show()
    #executes and ends the app when the system decides to
    sys.exit(app.exec_())
