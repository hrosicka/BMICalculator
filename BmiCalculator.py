import sys

from pathlib import Path

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMessageBox,
)

from PyQt5.QtGui import (
    QIcon,
    QRegExpValidator,
    QValidator,
)

from PyQt5 import QtCore

# for importing GUI - created by QtDesigner
from PyQt5.uic import loadUi

# methods for calculation BMI
import BMI


class Formular(QDialog):

    # static variables for information about person
    user_person_age = ""
    user_person_height = ""
    user_person_weight = ""
    user_person_result = ""
    user_person_gender = "Male"
    user_person_result_classification = ""

    # init main dialog
    def __init__(self):
        
        super().__init__()

        # loading UI - created by QtDesigner
        loadUi("dialog.ui", self)

        # input validation - regular expression
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{1,2})|([1-9][0-9]{1,2}[.])|([1-9][0-9]{1,2}[.][0-9]{1,3})'))

        self.edit_age.setValidator(validator_possitive)
        self.edit_height.setValidator(validator_possitive)
        self.edit_weight.setValidator(validator_possitive)

        # buttons
        self.button_clear.clicked.connect(lambda: self.clear_inputs())
        self.button_close.clicked.connect(app.closeAllWindows)
        self.button_calculate.clicked.connect(lambda: self.calculate_bmi())
        self.button_more.clicked.connect(lambda: self.more_info())

        # age input
        self.edit_age.textChanged.connect(lambda: self.check_state("age"))
        self.edit_age.textChanged.connect(self.clear_results)
        self.edit_age.textChanged.emit(self.edit_age.text())

        # height input in cm
        self.edit_height.textChanged.connect(lambda: self.check_state("height"))
        self.edit_height.textChanged.connect(self.clear_results)
        self.edit_height.textChanged.emit(self.edit_height.text())

        # weight input in cm
        self.edit_weight.textChanged.connect(lambda: self.check_state("weight"))
        self.edit_weight.textChanged.connect(self.clear_results)
        self.edit_weight.textChanged.emit(self.edit_weight.text())

        # gender radio button
        self.radio_male.toggled.connect(self.clear_results)
        self.radio_female.toggled.connect(self.clear_results)

        # stylesheet for results
        self.edit_result.setStyleSheet('QLineEdit { color: rgb(209, 209, 209); font: 16pt} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        
        # stylesteet for buttons
        self.button_more.setStyleSheet('QPushButton { color: rgb(69, 206, 86); border-color: rgb(58, 58, 58)} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

        self.button_clear.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_close.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_calculate.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

        # read data from static variables                                     
        self.fill_data()


    # fill data form static variables
    def fill_data(self):
        self.edit_age.setText(str(Formular.user_person_age))
        self.edit_height.setText(str(Formular.user_person_height))
        self.edit_weight.setText(str(Formular.user_person_weight))
        self.edit_result.setText(str(Formular.user_person_result))
        if (Formular.user_person_gender == "Male"):
            self.radio_male.setChecked(True)
        if (Formular.user_person_gender == "Female"):
            self.radio_female.setChecked(True)

    # more info works only if the results exists
    def more_info(self):
        # works only if the result exists
        if (Formular.user_person_result != ""):
            info_BMI =  InfoFormular()
            widget.addWidget(info_BMI)
            widget.setCurrentIndex(widget.currentIndex()+1)

    # clear all inputs in edit boxes and setup stati variables = ""
    def clear_inputs(self):
        self.edit_age.clear()
        self.edit_height.clear()
        self.edit_weight.clear()
        self.edit_result.clear()
        Formular.user_person_age = ""
        Formular.user_person_height = ""
        Formular.user_person_weight = ""
        Formular.user_person_result = ""
        Formular.user_person_result_classification = ""

    # clear results
    def clear_results(self):
        self.edit_result.clear()

    # calculate bmi
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
            Formular.user_person_result_classification = BMI.return_results(float(Formular.user_person_result))
    
    def check_state(self, field_name):

        if field_name == "age":
            edit_field = self.edit_age
        elif field_name == "height":
            edit_field = self.edit_height
        elif field_name == "weight":
            edit_field = self.edit_weight
        else:
            return  # Error: unknown field_name

        validator = edit_field.validator()
        state = validator.validate(edit_field.text(), 0)[0]
        if edit_field.text() == "0" or edit_field.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        edit_field.setStyleSheet('QLineEdit { background-color: %s; font: 16pt} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}' % color)


# second dialog for informatin display
class InfoFormular(QDialog):

    def __init__(self):
        super().__init__()
        # loading design - created in QtCreator
        loadUi("info_dialog.ui", self)

        # buttons - connection
        self.button_back.clicked.connect(lambda: self.go_main())
        self.button_clear.clicked.connect(lambda: self.clear_data())
        self.button_close.clicked.connect(app.closeAllWindows)

        # displaying results
        output0 = "Information about you:"
        output1 = "You are " + str(Formular.user_person_age) + " years old."
        output2 = "Your height is " + str(Formular.user_person_height) + " cm."
        output3 = "Your weight is " + str(Formular.user_person_weight) + " kg."
        output4 = "Your BMI is " + str(Formular.user_person_result) + "."
        output5 = "Your classification is " + str(Formular.user_person_result_classification)

        self.information = output0 + "\n" + output1 + "\n" + output2 + "\n" + output3 + "\n" + output4 + "\n" + output5
        self.show_info()

        # button stylesheet
        self.button_back.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_close.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_clear.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

    # return to main window
    def go_main(self):
        mainwindow = Formular()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_info(self):
        self.text_show.setText(self.information)
        
    def clear_data(self):
        Formular.user_person_age = ""
        Formular.user_person_height = ""
        Formular.user_person_weight = ""
        Formular.user_person_result = ""
        self.text_show.clear()

app = QApplication(sys.argv)
mainwindow = Formular()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('BMI Calculator')
widget.setWindowIcon(QIcon('Pig.png'))
widget.addWidget(mainwindow)
widget.show()
app.setStyleSheet(Path('bmi.qss').read_text())
app.exec()