class Requirement:
    type: int

    def __init__(self, impossible_values: list = None, possible_values: list = None):
        self.impossible_values: list = impossible_values
        self.possible_values: list = possible_values

    def get_requirement_types_dict(self):
        requirement_types_dict = {}
        for requirement_type in type(self).__subclasses__():
            requirement_types_dict[requirement_type.type] = requirement_type

    def check_value(self, value) -> bool:
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


class PhoneRequirement(Requirement):
    pass


class GeoRequirement(Requirement):
    pass


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





