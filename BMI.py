def indexBMI(weight, height):
    """
    Calculates Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Raises:
        TypeError: If weight or height is not a number.
        ValueError: If weight or height is non-positive.

    Returns:
        float: Calculated BMI value.
    """
    try:
        weight = float(weight)
        height = float(height)
    except ValueError as e:
        raise TypeError("Weight and height must be numeric values.") from e

    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    return weight / height**2


def return_results(bmi):
    """"
    Classifies BMI based on WHO guidelines.

    Args:
        bmi (float): Calculated BMI value.

    Returns:
        str: BMI classification.
    """
    # dictionary is used for classification of BMI
    classification = {
    "Underweight.": (bmi < 18.5),
    "Normal.": (18.5 <= bmi < 25),
    "Overweight.": (25 <= bmi < 30),
    "Obese Class I.": (30 <= bmi < 35),
    "Obese Class II.": (35 <= bmi < 40),
    "Obese Class III.": (bmi >= 40),
    }

    for k, v in classification.items():
        if v:
            return k
    
def main():
    """
    Calculates and classifies BMI for a given weight and height.
    """
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = indexBMI(weight, height)

    # Print BMI and classification
    print(f"Your BMI is {bmi}")
    print(f"BMI Classification: {return_results(bmi)}")

if __name__ == "__main__":
    main()