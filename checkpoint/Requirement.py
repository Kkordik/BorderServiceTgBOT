from aiogram.types import KeyboardButton
from texts import but_texts


class Requirement:
    keyboard_button: KeyboardButton
    type: int

    def __init__(self, impossible_values: list = None, possible_values: list = None):
        self.impossible_values: list = impossible_values
        self.possible_values: list = possible_values

    def get_requirement_types_dict(self) -> dict:
        requirement_types_dict = {0: NotRequired}

        for requirement_type in type(self).__subclasses__():
            requirement_types_dict[requirement_type.type] = requirement_type
        return requirement_types_dict

    def check_value(self, value) -> bool:
        if value is None:
            return False

        if self.possible_values:
            if value in self.possible_values:
                return True
            else:
                return False

        elif self.impossible_values:
            if value not in self.impossible_values:
                return True
            else:
                return False

    def keyboard_button(self, lang: str) -> KeyboardButton:
        pass


class NotRequired(Requirement):
    type = 0

    def check_value(self, value) -> bool:
        return False


class PhoneRequirement(Requirement):
    def keyboard_button(self, lang: str) -> KeyboardButton:
        return KeyboardButton(but_texts[lang]['phone'])


class GeoRequirement(Requirement):
    def keyboard_button(self, lang: str) -> KeyboardButton:
        return KeyboardButton(but_texts[lang]['location'])


class NotRuPhone(PhoneRequirement):
    type = 1

    def __init__(self):
        super().__init__(impossible_values=['RU', 'NAC'])


class OnlyUAPhone(PhoneRequirement):
    type = 2

    def __init__(self):
        super().__init__(possible_values=['UA'])


class NotRuGeo(GeoRequirement):
    type = 1

    def __init__(self):
        super().__init__(impossible_values=['RU', 'NAC'])


class OnlyUAGeo(GeoRequirement):
    type = 2

    def __init__(self):
        super().__init__(possible_values=['UA'])
