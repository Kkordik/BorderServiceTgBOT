import aiohttp


class GeoPosition:
    __url = "https://nominatim.openstreetmap.org/"

    def __init__(self, latitude, longitude, country_data=None, country_code=None):
        self._latitude = latitude
        self._longitude = longitude
        self.__country_data = country_data
        self.country_code = country_code

    async def get_country_data(self):
        url = self.__url + f"reverse?format=json&lat={self._latitude}&lon={self._longitude}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                self.__country_data = data
        return self.__country_data

    async def get_country_code(self):
        if not self.__country_data:
            await self.get_country_data()

        self.country_code = self.__country_data['address']['country_code']
        return self.country_code
