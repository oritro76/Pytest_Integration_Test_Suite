from typing import Optional, Tuple, Union
from faker import Faker
from device_settings.settings import MAX_BRIGHTNESS_LEVEL


class RandomDataGenerator:
    """
    A class to generate random data for testing purposes using the Faker library.
    """

    def __init__(self) -> None:
        """
        Initializes the RandomDataGenerator with a Faker instance.
        """
        self.faker = Faker()

    def random_private_ip(self) -> str:
        """
        Generates a random private IPv4 address.

        Returns:
            str: A random private IPv4 address.
        """
        return self.faker.ipv4(private="private")

    def random_name(self) -> str:
        """
        Generates a random name.

        Returns:
            str: A random name.
        """
        return self.faker.name()
    
    def invalid_names(self) -> Tuple[Optional[Union[str, int]], ...]:
        """
        Generates a tuple of invalid names for testing purposes.

        Returns:
            Tuple[Optional[Union[str, int]], ...]: A tuple containing various invalid names.
        """
        return (
            "", 
            None, 
            self.faker.pystr(min_chars=500, max_chars=600),
            "name_with_special_chars!@#",
            12345,
        )

    def random_color(self) -> str:
        """
        Generates a random hexadecimal color code.

        Returns:
            str: A random hexadecimal color code.
        """
        return self.faker.hex_color()

    def invalid_colors(self) -> Tuple[Optional[Union[str, int]], ...]:
        """
        Generates a tuple of invalid color codes for testing purposes.

        Returns:
            Tuple[Optional[Union[str, int]], ...]: A tuple containing various invalid color codes.
        """
        return (
            "00ff00",       # Missing '#'
            "#00ff00ff",    # Too long
            "#gggggg",      # Invalid characters
            "",             # Empty string
            self.faker.pystr(min_chars=5, max_chars=10), #random string
            None,           # null value
            "#00ff0@",      # Special characters
            "#00ff",        # Incorrect length
            self.faker.pyint(), #random integer
        )

    def random_brightness(self, right_digits: int = 2, min_value: int = 0, max_value: int = MAX_BRIGHTNESS_LEVEL) -> float:
        """
        Generates a random brightness level within the valid range.

        Args:
            right_digits (int, optional): Number of digits to the right of the decimal point. Defaults to 2.
            min_value (int, optional): Minimum value for brightness. Defaults to 0.
            max_value (int, optional): Maximum value for brightness. Defaults to MAX_BRIGHTNESS_LEVEL.

        Returns:
            float: A random brightness level.
        """
        return self.faker.pyfloat(
            right_digits=right_digits, min_value=min_value, max_value=max_value
        )

    def random_invalid_brightness_greater_than_max_val(
        self, right_digits: int = 2, min_value: int = MAX_BRIGHTNESS_LEVEL + 1, max_value: int = 100
    ) -> float:
        """
        Generates a random brightness level greater than the maximum valid value.

        Args:
            right_digits (int, optional): Number of digits to the right of the decimal point. Defaults to 2.
            min_value (int, optional): Minimum value for brightness. Defaults to MAX_BRIGHTNESS_LEVEL + 1.
            max_value (int, optional): Maximum value for brightness. Defaults to 100.

        Returns:
            float: An invalid brightness level greater than the maximum valid value.
        """
        return self.faker.pyfloat(
            right_digits=right_digits, min_value=min_value, max_value=max_value
        )

    def random_invalid_brightness_lower_than_min_val(
        self, right_digits: int = 2, min_value: int = 0, max_value: int = 100
    ) -> float:
        """
        Generates a random brightness level lower than the minimum valid value.

        Args:
            right_digits (int, optional): Number of digits to the right of the decimal point. Defaults to 2.
            min_value (int, optional): Minimum value for brightness. Defaults to 0.
            max_value (int, optional): Maximum value for brightness. Defaults to 100.

        Returns:
            float: An invalid brightness level lower than the minimum valid value.
        """
        return -self.faker.pyfloat(
            right_digits=right_digits, min_value=min_value, max_value=max_value
        )
    
    def random_json(self) -> str:
        """
        Generates a random JSON string.

        Returns:
            str: A random JSON string.
        """
        return self.faker.json()
