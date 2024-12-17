import unittest
import sys

# Setting the path to the module to be tested
sys.path.append('../BmiCalculator')
from BMI import indexBMI

class TestBMI(unittest.TestCase):

    def test_positive_bmi(self):
        """Tests BMI calculation with positive inputs."""
        weight = 70.0
        height = 1.75
        expected_bmi = 22.86
        bmi = indexBMI(weight, height)
        self.assertAlmostEqual(bmi, expected_bmi, places=2)

    def test_zero_weight(self):
        """Tests BMI calculation with zero weight."""
        weight = 0.0
        height = 1.75
        with self.assertRaises(ValueError):
            indexBMI(weight, height)

    def test_negative_weight(self):
        """Tests BMI calculation with negative weight."""
        weight = -70.0
        height = 1.58
        with self.assertRaises(ValueError):
            indexBMI(weight, height)

    def test_zero_height(self):
        """Tests BMI calculation with zero height."""
        weight = 54.0
        height = 0.0
        with self.assertRaises(ValueError):
            indexBMI(weight, height)

    def test_negative_height(self):
        """Tests BMI calculation with negative height."""
        weight = 65.0
        height = -1.62
        with self.assertRaises(ValueError):
            indexBMI(weight, height)

    def test_non_numeric_weight(self):
        """Tests BMI calculation with non-numeric weight."""
        weight = "Hello"
        height = 1.58
        with self.assertRaises(TypeError):
            indexBMI(weight, height)

    def test_non_numeric_height(self):
        """Tests BMI calculation with non-numeric height."""
        weight = 73.0
        height = "World"
        with self.assertRaises(TypeError):
            indexBMI(weight, height)

if __name__ == '__main__':
    unittest.main()

