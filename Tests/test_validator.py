import unittest
import sys

# Setting the path to the module to be tested
sys.path.append('../BmiCalculator')
from validator import Validator

class ValidatorTest(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test fixture by creating a Validator instance.
        """
        self.validator = Validator()

    def test_validate_weight_valid_range(self):
        """
        Tests if the validate_weight method returns True for valid weight values within the specified range.
        """
        self.assertTrue(self.validator.validate_weight("45"))
        self.assertTrue(self.validator.validate_weight("300"))
        self.assertTrue(self.validator.validate_weight("150.525"))

    def test_validate_weight_invalid_range(self):
        """
        Tests if the validate_weight method returns False for invalid weight values outside the specified range.
        """
        self.assertFalse(self.validator.validate_weight("39.785"))
        self.assertFalse(self.validator.validate_weight("301"))
        self.assertFalse(self.validator.validate_weight("0.0"))

    def test_validate_weight_invalid_input(self):
        """
        Tests if the validate_weight method returns False for invalid non-numeric input.
        """
        self.assertFalse(self.validator.validate_weight("abc"))
        self.assertFalse(self.validator.validate_weight(""))

    def test_validate_age_valid_range(self):
        """
        Tests if the validate_age method returns True for valid age values within the specified range.
        """
        self.assertTrue(self.validator.validate_age("10.785456"))
        self.assertTrue(self.validator.validate_age("120"))
        self.assertTrue(self.validator.validate_age("50"))

    def test_validate_age_invalid_range(self):
        """
        Tests if the validate_age method returns False for invalid age values outside the specified range.
        """
        self.assertFalse(self.validator.validate_age("9"))
        self.assertFalse(self.validator.validate_age("121"))
        self.assertFalse(self.validator.validate_age("-107217"))

    def test_validate_age_invalid_input(self):
        """
        Tests if the validate_age method returns False for invalid non-numeric input.
        """
        self.assertFalse(self.validator.validate_age("abc"))
        self.assertFalse(self.validator.validate_age(""))

    def test_validate_height_valid_range(self):
        """
        Tests if the validate_height method returns True for valid height values within the specified range.
        """
        self.assertTrue(self.validator.validate_height("100"))
        self.assertTrue(self.validator.validate_height("250"))
        self.assertTrue(self.validator.validate_height("175.57"))

    def test_validate_height_invalid_range(self):
        """
        Tests if the validate_height method returns False for invalid height values outside the specified range.
        """
        self.assertFalse(self.validator.validate_height("99"))
        self.assertFalse(self.validator.validate_height("251"))
        self.assertFalse(self.validator.validate_height("-777"))

    def test_validate_height_invalid_input(self):
        """
        Tests if the validate_height method returns False for invalid non-numeric input.
        """
        self.assertFalse(self.validator.validate_height("abc"))
        self.assertFalse(self.validator.validate_height(""))

if __name__ == '__main__':
    unittest.main()

