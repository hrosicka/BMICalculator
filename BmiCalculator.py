# Import libraries
import sys
from pathlib import Path
from PyQt5 import QtWidgets

# Import specific classes from PyQt5 for GUI creation and functionalities
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

# Import for loading UI elements created with Qt Designer
from PyQt5.uic import loadUi

# Import modules for BMI calculation and user data storage
import BMI
import user as usr
from validator import Validator


class Formular(QDialog):
    """
    This class represents the main window of the BMI calculator application.
    It handles user interaction, input validation, BMI calculation, and result display.
    """

    # init main dialog
    def __init__(self, user=None):
        """
        Constructor for the Formular class.

        Args:
            user (User, optional): An optional User object containing user data. Defaults to None.
        """
        super().__init__()

        # Create a user object to store information (if user argument is not provided)
        if user is None:
            self.user = usr.User() 
        else:
            self.user = user

        self.validator = Validator()

        # Load UI elements from a ".ui" file created with Qt Designer
        loadUi("dialog.ui", self)

        # Set up regular expression validators for positive numbers with specific format
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{1,2})|([1-9][0-9]{1,2}[.])|([1-9][0-9]{1,2}[.][0-9]{1,3})'))

        self.edit_age.setValidator(validator_possitive)
        self.edit_height.setValidator(validator_possitive)
        self.edit_weight.setValidator(validator_possitive)

         # Connect buttons to functions
        self.button_clear.clicked.connect(lambda: self.clear_inputs())
        self.button_close.clicked.connect(app.closeAllWindows)
        self.button_calculate.clicked.connect(lambda: self.calculate_bmi())
        self.button_more.clicked.connect(lambda: self.more_info())

        # Button for age input
        self.edit_age.textChanged.connect(lambda: self.check_state("age"))
        self.edit_age.textChanged.connect(self.clear_results)
        self.edit_age.textChanged.emit(self.edit_age.text())

        # Button for height input in cm
        self.edit_height.textChanged.connect(lambda: self.check_state("height"))
        self.edit_height.textChanged.connect(self.clear_results)
        self.edit_height.textChanged.emit(self.edit_height.text())

        # Button for weight input in cm
        self.edit_weight.textChanged.connect(lambda: self.check_state("weight"))
        self.edit_weight.textChanged.connect(self.clear_results)
        self.edit_weight.textChanged.emit(self.edit_weight.text())

        # Gender radio button
        self.radio_male.toggled.connect(self.clear_results)
        self.radio_female.toggled.connect(self.clear_results)

        # Set stylesheets for the results edit line and buttons
        self.edit_result.setStyleSheet('QLineEdit { color: rgb(209, 209, 209); font: 16pt} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_more.setStyleSheet('QPushButton { color: rgb(69, 206, 86); border-color: rgb(58, 58, 58)} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_clear.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_close.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_calculate.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

        # fill data from object user                              
        self.fill_data()

        if self.edit_result.text() != "":
            self.button_more.setEnabled(True)


    # Fill data from user object
    def fill_data(self):
        """
        Fills the input fields with data from the user object.
        """
        self.edit_age.setText(str(self.user.age))
        self.edit_height.setText(str(self.user.height_cm))
        self.edit_weight.setText(str(self.user.weight_kg))
        if (self.user.gender == "Male"):
            self.radio_male.setChecked(True)
        elif (self.user.gender == "Female"):
            self.radio_female.setChecked(True)
        self.edit_result.setText(str(self.user.bmi))

    # Show more info (works only if results exist)
    def more_info(self):
        """
        Shows a second window with detailed information about the user's BMI
        (only if a BMI result exists).
        """
        # works only if the result exists
        if (self.user.bmi != ""):
            info_BMI =  InfoFormular(self.user)
            widget.addWidget(info_BMI)
            widget.setCurrentIndex(widget.currentIndex()+1)

    # Clear all inputs in edit boxes and setup user variables to ""
    def clear_inputs(self):
        """
        Clears all input fields and resets user variables to empty strings.
        """
        self.edit_age.clear()
        self.edit_height.clear()
        self.edit_weight.clear()
        self.edit_result.clear()
        self.user.age = ""
        self.user.height_cm = ""
        self.user.weight_kg = ""
        self.user.bmi = ""
        self.user.classification = ""

    # Clear results
    def clear_results(self):
        """
        Clears the BMI result field and disables the "More Info" button.
        """
        self.edit_result.clear()
        self.button_more.setEnabled(False)


    def calculate_bmi(self):
        """
        Calculates BMI based on user input, validates data, and displays results
        or error messages.
        """
        if not self.validate_input():
            return

        # Extract values from UI
        age = float(self.edit_age.text())
        height_cm = float(self.edit_height.text())
        weight_kg = float(self.edit_weight.text())
        gender = "Male" if self.radio_male.isChecked() else "Female"

        # Calculate BMI
        bmi = BMI.indexBMI(weight_kg, height_cm / 100)

        # Update user data and UI
        self.user.age = age
        self.user.height_cm = height_cm
        self.user.weight_kg = weight_kg
        self.user.gender = gender
        self.user.bmi = round(bmi, 3)
        self.user.classification = BMI.return_results(bmi)
        self.edit_result.setText(str(self.user.bmi))
        self.button_more.setEnabled(True)

    def validate_input(self):
        """
        Validates user input for age, height, and weight.
        Displays error messages for invalid input.

        Returns:
            bool: True if all input is valid, False otherwise.
        """
        if not self.edit_age.text() or not self.edit_height.text() or not self.edit_weight.text():
            self.show_error_message("<FONT COLOR='#ffffff'>Please fill in all fields!")
            return False

        if not self.validator.validate_age(self.edit_age.text()):
            self.show_error_message("<FONT COLOR='#ffffff'>Age must be between 10 and 120!")
            return False

        if not self.validator.validate_height(self.edit_height.text()):
            self.show_error_message("<FONT COLOR='#ffffff'>Height must be between 100 and 250 cm!")
            return False

        if not self.validator.validate_weight(self.edit_weight.text()):
            self.show_error_message("<FONT COLOR='#ffffff'>Weight must be between 40 and 300 kg!")
            return False

        return True

    def show_error_message(self, message):
        """
        Displays a generic error message with the provided message.
        """
        messagebox = QMessageBox(QMessageBox.Warning, "Error", message, buttons=QMessageBox.Ok, parent=self)
        messagebox.exec_()

    
    def check_state(self, field_name):
        """
        Checks the state (validity) of a specific input field (age, height, or weight)
        based on the user's input. Updates the background color of the field accordingly.

        Args:
            field_name (str): The name of the field to check ("age", "height", or "weight").
        """
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
            color = '#FFC8CB' # red
        elif state == QValidator.Acceptable:
            color = '#E5F9C6' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#FFC8CB' # red
        edit_field.setStyleSheet('QLineEdit { background-color: %s; font: 16pt} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}' % color)


# Second dialog for informatin display
class InfoFormular(QDialog):

    def __init__(self, user):
        """
        Constructor for the InfoFormular class.

        Args:
            user: An instance of the User class containing user data.
        """

        super().__init__()
        self.user = user

        # Load UI elements from a ".ui" file created with Qt Designer
        loadUi("info_dialog.ui", self)

        # Connect buttons to functions
        self.button_back.clicked.connect(lambda: self.go_main())
        self.button_clear.clicked.connect(lambda: self.clear_data())
        self.button_close.clicked.connect(app.closeAllWindows)

        # Format a string to display detailed user information in the second window
        self.information = self.format_user_info(self.user.age, 
                                    self.user.height_cm, 
                                    self.user.weight_kg, 
                                    self.user.bmi, 
                                    self.user.classification)
        
        # Call the show_info function to display the information
        self.show_info()

        # Set stylesheets for the buttons
        self.button_back.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_close.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.button_clear.setStyleSheet('QPushButton { font: 12pt "MS Shell Dlg 2"; background-color: rgb(69, 206, 86); color: rgb(58, 58, 58); border-radius: 10px;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')


    def format_user_info(self, age, height, weight, bmi, classification):
        """
        Formats a string to display user information in a readable way.

        Args:
            age: User's age (float).
            height: User's height in centimeters (float).
            weight: User's weight in kilograms (float).
            bmi: User's Body Mass Index (float).
            classification: User's BMI classification (string).

        Returns:
            A formatted string containing user information.
        """
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
        """
        Returns to the main window (Formular class).

        Creates a new instance of Formular, adds it to the stack widget,
        and changes the current index to display the main window.
        """
        mainwindow = Formular(self.user)
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_info(self):
        """
        Sets the text of the text_show label to the formatted user information string.
        """
        self.text_show.setText(self.information)
        
    def clear_data(self):
        """
        Clears user data and the text displayed in the second window.

        Sets user attributes (age, height, weight, bmi, classification) to empty strings.
        Clears the text of the text_show label.
        """
        self.user.age = ""
        self.user.height_cm = ""
        self.user.weight_kg = ""
        self.user.bmi = ""
        self.user.classification = ""
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