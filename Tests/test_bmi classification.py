import unittest
import sys

# Setting the path to the module to be tested
sys.path.append('../BmiCalculator')
from BMI import return_results

class TestBMIClassification(unittest.TestCase):

    def test_underweight(self):
        """Tests classification for underweight BMI."""
        bmi = 17.0
        classification = return_results(bmi)
        self.assertEqual(classification, "Underweight.")

    def test_normal(self):
        """Tests classification for normal BMI."""
        bmi = 22.5
        classification = return_results(bmi)
        self.assertEqual(classification, "Normal.")

    def test_overweight(self):
        """Tests classification for overweight BMI."""
        bmi = 28.0
        classification = return_results(bmi)
        self.assertEqual(classification, "Overweight.")

    def test_obese_class_i(self):
        """Tests classification for obese class I BMI."""
        bmi = 32.0
        classification = return_results(bmi)
        self.assertEqual(classification, "Obese Class I.")

    def test_obese_class_ii(self):
        """Tests classification for obese class II BMI."""
        bmi = 37.0
        classification = return_results(bmi)
        self.assertEqual(classification, "Obese Class II.")

    def test_obese_class_iii(self):
        """Tests classification for obese class III BMI."""
        bmi = 42.0
        classification = return_results(bmi)
        self.assertEqual(classification, "Obese Class III.")

if __name__ == '__main__':
    unittest.main()

