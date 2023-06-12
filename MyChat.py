from aiogram.types import Chat
from Table import Table, Database
from checkpoint.Requirement import PhoneRequirement, GeoRequirement

class ChatsTable(Table):
    """
    chat_id	bigint
    date_time	datetime
    username	tinytext
    require_phone	tinyint
    require_position	tinyint
    require_language	tinyint
    """
    __name = "chats"
    __columns = ["chat_id", "date_time", "username", "require_phone", "require_position", "require_language"]

    def __init__(self, db: Database):
        super().__init__(self.__name, db, self.__columns)


class MyChat:
    def __init__(self, table: ChatsTable, chat_id, chat: Chat = None, chat_data: dict = None,
                 phone_requirement: PhoneRequirement = None, geo_requirement: GeoRequirement = None):
        self._table: ChatsTable = table
        self._chat: Chat = chat
        self._chat_id = chat_id
        self._chat_data: dict = chat_data
        self.phone_requirement: PhoneRequirement = phone_requirement
        self.geo_requirement: GeoRequirement = geo_requirement

    def get_chat_data(self):
        return self._chat_data

    def set_chat_data(self, new_chat_data):
        if isinstance(new_chat_data, list):
            self._chat_data = new_chat_data[0]
        elif isinstance(new_chat_data, dict):
            self._chat_data = new_chat_data
        else:
            raise Exception(f'Impossible to set {type(new_chat_data)} as chat_data')

    async def find_chat_data(self):
        self.set_chat_data(await self._table.select_vals(chat_id=int(self._chat_id)))
        return self._chat_data

    async def insert_chat(self, **values):
        print(self._chat_id)
        return await self._table.insert_vals(chat_id=int(self._chat_id), **values)
