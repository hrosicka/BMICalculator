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
import user


class Formular(QDialog):

    # Create a user object to store information
    user = user.User()  

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
        self.edit_age.setText(str(Formular.user.age))
        self.edit_height.setText(str(Formular.user.height_cm))
        self.edit_weight.setText(str(Formular.user.weight_kg))
        self.edit_result.setText(str(Formular.user.bmi))
        if (self.user.gender == "Male"):
            self.radio_male.setChecked(True)
        if (self.user.gender == "Female"):
            self.radio_female.setChecked(True)

    # more info works only if the results exists
    def more_info(self):
        # works only if the result exists
        if (Formular.user.bmi != ""):
            info_BMI =  InfoFormular()
            widget.addWidget(info_BMI)
            widget.setCurrentIndex(widget.currentIndex()+1)

    # clear all inputs in edit boxes and setup stati variables = ""
    def clear_inputs(self):
        self.edit_age.clear()
        self.edit_height.clear()
        self.edit_weight.clear()
        self.edit_result.clear()
        Formular.user.age = ""
        Formular.user.height_cm = ""
        Formular.user.weight_kg = ""
        Formular.user.bmi = ""
        Formular.user.classification = ""

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
            Formular.user.age = float(self.edit_age.text())
            Formular.user.height_cm = float(self.edit_height.text())
            Formular.user.weight_kg = float(self.edit_weight.text())
            if self.radio_male.isChecked() == True:
                Formular.user.gender = "Male"
            if self.radio_female.isChecked() == True:
                Formular.user.gender = "Female"
            Formular.user.bmi = round(BMI.indexBMI(Formular.user.weight_kg, Formular.user.height_cm/100),3)
            self.edit_result.setText(str(Formular.user.bmi))
            Formular.user.classification = BMI.return_results(float(Formular.user.bmi))
    
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

        # formated string for displaying results in second window - detailed results
        self.information = self.format_user_info(Formular.user.age, 
                                    Formular.user.height_cm, 
                                    Formular.user.weight_kg, 
                                    Formular.user.bmi, 
                                    Formular.user.classification)
        self.show_info()

        # button stylesheet
        self.button_back.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_close.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_clear.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

    # formated string for displaying results in second window - detailed results
    def format_user_info(self, age, height, weight, bmi, classification):
        if isinstance(age, str):
            age = float(age)
        height = float(height)
        weight = float(weight)
        bmi = float(bmi)
        return f"""Information about you:
You are {age} years old.
Your height is {height} cm.
Your weight is {weight} kg.
Your BMI is {bmi:.2f}.
Your classification is {classification}
        """

    # return to main window
    def go_main(self):
        mainwindow = Formular()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_info(self):
        self.text_show.setText(self.information)
        
    def clear_data(self):
        Formular.user.age = ""
        Formular.user.height_cm = ""
        Formular.user.weight_kg = ""
        Formular.user.bmi = ""
        Formular.user.classification = ""
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