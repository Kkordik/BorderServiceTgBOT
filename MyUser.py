from run_bot import bot
from aiogram.types import User
from texts import but_texts


class MyUser:
    def __init__(self, user_id, user: User = None, lang: str = None):
        self._user: User = user
        self._user_id = user_id
        self._lang = lang

    def get_lang(self):
        return self._lang

    def set_lang(self, lang: str):
        self._lang = self._adjust_lang(lang)

    def get_user(self):
        return self._user

    def set_user(self, user: User):
        self._user = user

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
        self._lang = self._adjust_lang(self._user.language_code)
        return self._lang
