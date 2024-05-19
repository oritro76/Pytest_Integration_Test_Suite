from faker import Faker
from tests.device_settings.settings import MAX_BRIGHTNESS_LEVEL


class RandomDataGenerator:
    def __init__(self):
        self.faker = Faker()

    def random_private_ip(self):
        return self.faker.ipv4(private="private")

    def random_name(self):
        return self.faker.name()
    
    def invalid_names(self):
        return (
                "",
                None,
                "a" * 256,
                "name_with_special_chars!@#",
                12345,
            )

    def random_color(self):
        return self.faker.hex_color()

    def invalid_colors(self):
        # Generating an obviously invalid color code for testing
        return (
                "00ff00",       # Missing '#'
                "#00ff00ff",    # Too long
                "#gggggg",      # Invalid characters
                "",             # Empty string
                None,           # None value
                "#00ff0@",      # Special characters
                "#00ff"         # Incorrect length
            )

    def random_brightness(self):
        return self.faker.pyfloat(
            right_digits=2, min_value=0, max_value=MAX_BRIGHTNESS_LEVEL
        )

    def random_invalid_brightness_greater_than_max_val(self):
        # Generating an invalid brightness value for testing
        return self.faker.pyfloat(right_digits=2, min_value=MAX_BRIGHTNESS_LEVEL + 1, max_value=100)
    
    def random_invalid_brightness_lower_than_min_val(self):
        # Generating an invalid brightness value for testing
        return -self.faker.pyfloat(right_digits=2, min_value=0, max_value=100)

