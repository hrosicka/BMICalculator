import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
)

from PyQt5.QtGui import (
    QPixmap, 
    QIcon,
)

from PyQt5 import QtCore

from PyQt5.uic import loadUi

import BMI


class Formular(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("dialog.ui", self)
        self.setWindowTitle('BMI Calculator')
        self.setWindowIcon(QIcon('Pig.png'))
        self.button_clear.clicked.connect(lambda: self.clear_inputs())
        self.button_close.clicked.connect(self.close)
        self.button_calculate.clicked.connect(lambda: self.calculate_bmi())

    def clear_inputs(self):
        self.edit_age.clear()
        self.edit_height.clear()
        self.edit_weight.clear()
        self.edit_result.clear()

    def calculate_bmi(self):
        person_height = float(self.edit_height.text())
        person_weight = float(self.edit_weight.text())
        person_result = BMI.indexBMI(person_weight, person_height/100)
        self.edit_result.setText(str(round(person_result,3)))
    
   
app = QApplication(sys.argv)
w = Formular()
w.show()
app.exec()