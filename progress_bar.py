from PyQt5 import QtWidgets
from PyQt5 import QtCore
from time import sleep
import sys, os


class MyCustomWidget(QtWidgets.QWidget):

    def __init__(self, task, parent=None):
        super(MyCustomWidget, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        # Create a progress bar and a button and add them to the main layout
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setRange(0, 1)
        layout.addWidget(self.progressBar)
        self.myLongTask = TaskThread(task)
        self.myLongTask.taskFinished.connect(self.onFinished)
        self.onStart()

    def onStart(self):
        self.progressBar.setRange(0, 0)
        self.myLongTask.start()

    def onFinished(self):
        # Stop the pulsation
        self.progressBar.setRange(0, 1)
        self.progressBar.setValue(1)


class TaskThread(QtCore.QThread):
    def __init__(self, task):
        super().__init__()
        self.task = task
    taskFinished = QtCore.pyqtSignal()

    def run(self):
        self.task()
        self.taskFinished.emit()

