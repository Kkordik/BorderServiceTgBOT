class Position:
    def __init__(self, country_code: str = None):
        self._country_code: str = country_code

    def set_country_code(self, new_country_code: str):
        self._country_code = new_country_code.upper()

    def get_country_code(self) -> str:
        return self._country_code

    async def find_country_code(self) -> str:
        return self._country_code
