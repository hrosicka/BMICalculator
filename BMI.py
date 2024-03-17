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

    bmi = round(indexBMI(52,1.57),2)
    print("BMI is", bmi)
    print(return_results(bmi))

if __name__ == "__main__":
    main()