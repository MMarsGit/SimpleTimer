from datetime import datetime
from PyQt5.QtWidgets import QLabel
#Get current time
def start_time():
    start = datetime.now()
    return start

#Get final time
def final_time():
    final = datetime.now()
    return final

#Update label
def update_label(startTime, label):
    current = datetime.now()
    labelElapsed = current - startTime
    label.setText(labelElapsed)

#Set timer thread updating button