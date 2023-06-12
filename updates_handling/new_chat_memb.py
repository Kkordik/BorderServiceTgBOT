import asyncio

from aiogram.types import Message, ContentType
from aiogram import Dispatcher
from run_bot import dp, bot
from keyboards import start_keyboard
from MyUser import MyUser
from texts import msg_texts


async def new_chat_member(message: Message):
    my_users = []

    for new_user in message.new_chat_members:

        my_user = MyUser(user_id=new_user.id, user=new_user)
        await my_user.find_lang()

        my_users.append(my_user)

        fulfills = False
        # User examination, checking if user fulfills the chat requirements
        if not fulfills:
            new_member_msg = await message.answer(
                text=msg_texts[my_user.get_lang()]['new_chat_member'].format(new_user.id, new_user.first_name),
                parse_mode='html',
                allow_sending_without_reply=True
            )
            await asyncio.sleep(30)
            await new_member_msg.delete()


def register_new_member_handler(dp: Dispatcher):
    dp.register_message_handler(new_chat_member, content_types=ContentType.NEW_CHAT_MEMBERS)
