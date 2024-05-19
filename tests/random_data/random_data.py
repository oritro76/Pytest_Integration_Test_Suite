from typing import Optional, Tuple, Union
from faker import Faker
from tests.device_settings.settings import MAX_BRIGHTNESS_LEVEL


class RandomDataGenerator:
    def __init__(self) -> None:
        self.faker = Faker()

    def random_private_ip(self) -> str:
        return self.faker.ipv4(private="private")

    def random_name(self) -> str:
        return self.faker.name()
    
    def invalid_names(self) -> Tuple[Optional[Union[str, int]], ...]:
        return (
            "",
            None,
            self.faker.pystr(min_chars=500, max_chars=600),
            "name_with_special_chars!@#",
            12345,
        )

    def random_color(self) -> str:
        return self.faker.hex_color()

    def invalid_colors(self) -> Tuple[Optional[Union[str, int]], ...]:
        return (
            "00ff00",       # Missing '#'
            "#00ff00ff",    # Too long
            "#gggggg",      # Invalid characters
            "",             # Empty string
            self.faker.pystr(min_chars=5, max_chars=10), 
            None,           # None value
            "#00ff0@",      # Special characters
            "#00ff",        # Incorrect length
            self.faker.pyint(),
        )

    def random_brightness(self) -> float:
        return self.faker.pyfloat(
            right_digits=2, min_value=0, max_value=MAX_BRIGHTNESS_LEVEL
        )

    def random_invalid_brightness_greater_than_max_val(self) -> float:
        return self.faker.pyfloat(right_digits=2, min_value=MAX_BRIGHTNESS_LEVEL + 1, max_value=100)
    
    def random_invalid_brightness_lower_than_min_val(self) -> float:
        return -self.faker.pyfloat(right_digits=2, min_value=0, max_value=100)
    
    def random_json(self) -> str:
        return self.faker.json()