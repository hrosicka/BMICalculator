# BMICalculator
This user-friendly application is a Body Mass Index (BMI) calculator that allows you to calculate your BMI and view additional information about your BMI classification. Simply enter your age, height, and weight, and get your BMI with clear classification. Stay informed about your weight status with our user-friendly BMI calculator!

## Main window
The main window consists of several sections:
- Input Fields:
  - Age: Enter your age in years.
  - Height: Enter your height in centimeters (cm).
  - Weight: Enter your weight in kilograms (kg).
  - Gender: Select your gender (Male or Female).

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/BmiCalculator.png)

- Validation:
  - The application validates your input as you type. The background color of the input field will change to:
    - Green: Valid input
    - Yellow: Potentially invalid input
    - Red: Invalid input
   
- Limits:
  - Limits are in place to ensure that the BMI calculation is accurate and reliable. If you enter a value outside of these limits, the application will display an error message. 
  
##### Age
Age must be filled.
The age limit is based on the fact that BMI is not a reliable measure of body fat for children under 10 years old or adults over 120 years old.
- Minimum: 10 years
- Maximum: 120 years

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/MissingAge.png)

##### Height
Height must be filled.
The height limit is based on the fact that BMI is not a reliable measure of body fat for people who are very short or very tall.
- Minimum: 100 cm
- Maximum: 250 cm

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/MissingHeight.png)

##### Weight
Weight must be filled.
The weight limit is based on the fact that BMI is not a reliable measure of body fat for people who are very thin or very heavy.
- Minimum: 40 kg
- Maximum: 300 kg

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/MissingWeight.png)

- Buttons:
  - More Info: (Initially disabled) This button becomes enabled only after a successful BMI calculation. Clicking this button opens a new window with detailed information about your BMI.
  - Clear: Clears all input fields and resets the results.
  - Calculate: Calculates your BMI based on your entered information.
  - Close: Closes the application.

## Calculating BMI
1. Enter your age, height, and weight in the corresponding fields.
2. Select your gender using the radio buttons.
3. Click the Calculate button.
  - If the input is valid, the application will calculate your BMI and display it in the results field.
  - If the input is invalid, the application will display an error message explaining the issue.

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/InputsOk.png)

## More Information
- After a successful BMI calculation, the More Info button becomes enabled.
- Clicking the More Info button opens a new window that displays detailed information about your BMI, including:
  - Your age, height, weight, and BMI.
  - Your BMI classification (e.g., Underweight, Normal Weight, Overweight, Obese).
    

![](https://github.com/hrosicka/PyQtBMICalculator/blob/master/doc/DetailedResults.png)

## Additional Features
- The application uses a stylesheet (bmi.qss) to customize the appearance of the windows and buttons.
- You can clear all your data and reset the application by clicking the Clear button.

  [MIT LICENSE](https://github.com/hrosicka/BMICalculator/blob/master/doc/LICENSE.txt)
