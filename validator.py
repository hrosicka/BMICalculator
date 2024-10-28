class Validator:
    
    def validate_weight(self, weight):
        """
        Validates the entered weight.

        Args:
            weight: The input weight value (string).

        Returns:
            True if the entered weight is in the range 40-300 kg, False otherwise.
        """

        # Attempts to convert the entered weight to a float.
        try:
            weight_float = float(weight)
        except ValueError:
            # If the conversion fails, returns False (invalid value).
            return False

        # Checks if the entered weight is in the range 40-300 kg.
        return 40 <= weight_float <= 300


    def validate_age(self, age):
        """
        Validates the entered age.

        Args:
            age: The input age value (string).

        Returns:
            True if the entered age is in the range 10-120, False otherwise.
        """

        # Attempts to convert the entered age to an integer.
        try:
            age_int = float(age)
        except ValueError:
            # If the conversion fails, returns False (invalid value).
            return False

        # Checks if the entered age is in the range 10-120.
        return 10 <= age_int <= 120
    

    def validate_height(self, height):
        """
        Validates the entered height.

        Args:
            height: The input height value (string).

        Returns:
            True if the entered height is in the range 100-250 cm, False otherwise.
        """

        # Attempts to convert the entered height to a float.
        try:
            height_float = float(height)
        except ValueError:
            # If the conversion fails, returns False (invalid value).
            return False

        # Checks if the entered height is in the range 100-250 cm.
        return 100 <= height_float <= 250