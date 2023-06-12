class Position:
    def __init__(self, country_code: str = None):
        self._country_code: str = self.adjust_country_code(country_code)

    @staticmethod
    def adjust_country_code(country_code):
        if isinstance(country_code, str):
            return country_code.upper()
        else:
            return country_code

    def set_country_code(self, new_country_code: str):
        self._country_code = self.adjust_country_code(new_country_code)

    def get_country_code(self) -> str:
        return self._country_code

    async def find_country_code(self) -> str:
        return self._country_code
