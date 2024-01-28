import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
)

from PyQt5.QtGui import (
    QPixmap, 
    QIcon,
    QRegExpValidator,
    QValidator,
)

from PyQt5 import QtCore

from PyQt5.uic import loadUi

import BMI


class Formular(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("dialog.ui", self)

        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{1,2})|([1-9][0-9]{1,2}[.])|([1-9][0-9]{1,2}[.][0-9]{1,3})'))

        self.edit_age.setValidator(validator_possitive)
        self.edit_height.setValidator(validator_possitive)
        self.edit_weight.setValidator(validator_possitive)

        self.button_clear.clicked.connect(lambda: self.clear_inputs())
        self.button_close.clicked.connect(self.close)
        self.button_calculate.clicked.connect(lambda: self.calculate_bmi())

        self.edit_age.textChanged.connect(self.check_state_age)
        self.edit_age.textChanged.emit(self.edit_age.text())

        self.edit_height.textChanged.connect(self.check_state_height)
        self.edit_height.textChanged.emit(self.edit_height.text())

        self.edit_weight.textChanged.connect(self.check_state_weight)
        self.edit_weight.textChanged.emit(self.edit_weight.text())

        self.button_more.clicked.connect(lambda: self.more_info())

    def more_info(self):
        info_BMI =  InfoFormular()
        widget.addWidget(info_BMI)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
    
    def check_state_age(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_age.text() == "0" or self.edit_age.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s; font: 16pt}' % color)


    def check_state_height(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_height.text() == "0" or self.edit_height.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s; font: 16pt}' % color)

    def check_state_weight(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_weight.text() == "0" or self.edit_weight.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s; font: 16pt}' % color)


class InfoFormular(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("info_dialog.ui", self)



app = QApplication(sys.argv)
mainwindow = Formular()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('BMI Calculator')
widget.setWindowIcon(QIcon('Pig.png'))
widget.addWidget(mainwindow)
widget.show()
app.exec()