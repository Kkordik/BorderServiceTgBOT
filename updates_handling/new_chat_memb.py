import aiogram.types

from run_bot import dp


def new_chat_member(message: aiogram.types.Message):
    print(update.__dict__)


def register_new_member_handler(dp: Dispatcher):
    dp.register_message_handler(new_chat_member, content_types=types.ContentType.NEW_CHAT_MEMBERS)


