def indexBMI(hmotnost, vyska):
    """
    Výpočet Body Mass Indexu

    hmotnost - hmotnost v kg

    vyska - vyska postavy v metrech
    """
    
    if hmotnost > 0 and vyska > 0:
        bmi = hmotnost / pow(vyska,2)
        return bmi

    else:
        raise ValueError("Hmotnost musí být kladné číslo.")

def return_results(bmi):
    """
    Klasifikace tělesné hmotnosti

    bmi - body mass index
    """

    if bmi < 18.5:
        return "Underweight."
    
    elif bmi >= 18.5 and bmi < 25:
        return "Normal."
    
    elif bmi >= 25 and bmi < 30:
        return "Overweight."
    
    elif bmi >= 30 and bmi < 35:
        return "Obese Class I."
    
    elif bmi >= 35 and bmi < 40:
        return "Obese Class II."
    
    elif bmi >= 40:
        return "Obese Class III."
    
def main():

    bmi = round(indexBMI(52,1.57),2)
    print("BMI is", bmi)
    print(return_results(bmi))

if __name__ == "__main__":
    main()