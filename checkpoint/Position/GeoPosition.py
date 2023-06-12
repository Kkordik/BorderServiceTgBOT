import aiohttp
from checkpoint.Position.Position import Position


class GeoPosition(Position):
    __url = "https://nominatim.openstreetmap.org/"

    def __init__(self, latitude=None, longitude=None, country_data=None, country_code: str = None):
        super().__init__(country_code=country_code)
        self._latitude = latitude
        self._longitude = longitude
        self._country_data = country_data

    async def _get_country_data(self):
        if not self._longitude or not self._latitude:
            raise Exception("No coordinates specified to get country_data")

        url = self.__url + f"reverse?format=json&lat={self._latitude}&lon={self._longitude}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                self._country_data = data
        return self._country_data

    async def find_country_code(self):
        if not self._country_data:
            await self._get_country_data()

        self.set_country_code(self._country_data['address']['country_code'])
        return self._country_code
