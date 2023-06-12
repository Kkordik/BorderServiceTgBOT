from run_bot import bot
from aiogram.types import User
from texts import but_texts
from Table import Table, Database
from checkpoint.Position.PhonePosition import PhonePosition
from checkpoint.Position.GeoPosition import GeoPosition


class UsersTable(Table):
    """
    user_id	bigint
    date_time	datetime
    phone_country	tinytext
    country_code	tinytext
    city	tinytext
    """
    __name = "users"
    __columns = ["user_id", "date_time", "phone_country", "country_code", "city"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class MyUser:
    def __init__(self, table: UsersTable, user_id, user: User = None, lang: str = None, user_data: dict = None,
                 phone_position: PhonePosition = None, geo_position: GeoPosition = None):
        self._table: UsersTable = table
        self._user: User = user
        self._user_id = user_id
        self._lang = lang
        self._user_data: dict = user_data
        self.phone_position: PhonePosition = phone_position
        self.geo_position: GeoPosition = geo_position

    def get_lang(self):
        return self._lang

    def set_lang(self, lang: str):
        self._lang = self._adjust_lang(lang)

    def get_user(self):
        return self._user

    def set_user(self, user: User):
        self._user = user

    def set_phone_position(self, phone_number: str) -> PhonePosition:
        self.phone_position = PhonePosition(phone_number=phone_number)
        return self.phone_position

    def set_geo_position(self,  latitude, longitude) -> GeoPosition:
        self.geo_position = GeoPosition(latitude=latitude, longitude=longitude)
        return self.geo_position

    def get_user_data(self):
        return self._user_data

    def set_user_data(self, new_user_data):
        if isinstance(new_user_data, list):
            self._user_data = new_user_data[0]
        elif isinstance(new_user_data, dict):
            self._user_data = new_user_data
        else:
            raise Exception(f'Impossible to set {type(new_user_data)} as user_data')

    async def find_user_data(self):
        self.set_user_data(await self._table.select_vals(user_id=int(self._user_id)))
        return self._user_data

    async def insert_user(self, **values):
        return await self._table.insert_vals(user_id=int(self._user_id), **values)

    @staticmethod
    def _adjust_lang(lang: str) -> str:
        if lang not in but_texts.keys():
            return 'en'
        else:
            return lang

    async def find_user(self) -> User:
        """
        Makes call to the bot and finds aiogram.User object
        :return: aiogram.User
        """
        if self._user:
            return self._user

        chat_member = await bot.get_chat_member(chat_id=self._user_id, user_id=self._user_id)
        self._user = chat_member.user
        return self._user

    async def find_lang(self) -> str:
        """
        Makes call to the bot and takes language_code from aiogram.User object,
        if self._user=None, finds it (aiogram.User)
        :return: aiogram.User.language_code
        """
        if self._lang:
            return self._lang

        self._user = await self.find_user()
        self.set_lang(self._user.language_code)
        return self._lang
