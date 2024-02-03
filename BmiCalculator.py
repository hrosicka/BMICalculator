import sys

from pathlib import Path

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox,
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

    user_person_age = ""
    user_person_height = ""
    user_person_weight = ""
    user_person_result = ""
    user_person_gender = "Male"

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

        self.fill_data()


    def fill_data(self):
        self.edit_age.setText(str(Formular.user_person_age))
        self.edit_height.setText(str(Formular.user_person_height))
        self.edit_weight.setText(str(Formular.user_person_weight))
        self.edit_result.setText(str(Formular.user_person_result))
        if (Formular.user_person_gender == "Male"):
            self.radio_male.setChecked(True)
        if (Formular.user_person_gender == "Female"):
            self.radio_female.setChecked(True)

    def more_info(self):
        if (Formular.user_person_result != ""):
            info_BMI =  InfoFormular()
            widget.addWidget(info_BMI)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def clear_inputs(self):
        self.edit_age.clear()
        self.edit_height.clear()
        self.edit_weight.clear()
        self.edit_result.clear()

    def calculate_bmi(self):

        if self.edit_age.text() in [""]:
            messagebox = QMessageBox(QMessageBox.Warning, "Error", "<FONT COLOR='#ffffff'> Age is missing!", buttons = QMessageBox.Ok, parent=self)
            messagebox.exec_()

        elif self.edit_height.text() in [""]:
            messagebox = QMessageBox(QMessageBox.Warning, "Error", "<FONT COLOR='#ffffff'> Height is missing!", buttons = QMessageBox.Ok, parent=self)
            messagebox.exec_()

        elif self.edit_weight.text() in [""]:
            messagebox = QMessageBox(QMessageBox.Warning, "Error", "<FONT COLOR='#ffffff'> Weight is missing!", buttons = QMessageBox.Ok, parent=self)
            messagebox.exec_()

        else:
            Formular.user_person_age = float(self.edit_age.text())
            Formular.user_person_height = float(self.edit_height.text())
            Formular.user_person_weight = float(self.edit_weight.text())
            if self.radio_male.isChecked() == True:
                Formular.user_person_gender = "Male"
            if self.radio_female.isChecked() == True:
                Formular.user_person_gender = "Female"
            Formular.user_person_result = round(BMI.indexBMI(Formular.user_person_weight, Formular.user_person_height/100),3)
            self.edit_result.setText(str(Formular.user_person_result))
    
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
        self.button_back.clicked.connect(lambda: self.go_main())
        output0 = "Information about you:"
        output1 = "Your height is " + str(Formular.user_person_height)
        output2 = "Your weight is " + str(Formular.user_person_weight)
        output3 = "Your BMI is " + str(Formular.user_person_result)

        self.information = output0 + "\n" + output1 + "\n" + output2 + "\n" + output3
        self.show_info()

    def go_main(self):
        mainwindow = Formular()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_info(self):
        self.text_show.setText(self.information)
        

app = QApplication(sys.argv)
mainwindow = Formular()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('BMI Calculator')
widget.setWindowIcon(QIcon('Pig.png'))
widget.addWidget(mainwindow)
widget.show()
app.setStyleSheet(Path('bmi.qss').read_text())
app.exec()