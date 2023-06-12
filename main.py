from checkpoint.location_check import register_location_handler
from checkpoint.phone_check import register_phone_handler
from new_user_handling.new_chat_memb import register_new_member_handler
from new_user_handling.join_request import register_join_req_handler
from checkpoint.Checkpoint import Checkpoint
from aiogram import types
from keyboards import start_keyboard
from MyUser import MyUser
from MyChat import MyChat
from run_bot import dp, bot
from run_db import USERS_TB, CHATS_TB
from texts import msg_texts
import asyncio


async def start_hand(message: types.Message):
    my_user = MyUser(table=USERS_TB, user_id=message.from_user.id, user=message.from_user)
    await my_user.insert_user()
    await my_user.find_lang()
    await message.answer(text=msg_texts[my_user.get_lang()]['start_msg'], reply_markup=start_keyboard(my_user.get_lang()))


async def start_hand_group(message: types.Message):
    my_user = MyUser(table=USERS_TB, user_id=message.from_user.id, user=message.from_user)
    await my_user.insert_user()
    await my_user.find_lang()

    my_chat = MyChat(table=CHATS_TB, chat_id=message.chat.id, chat=message.chat)
    await my_chat.insert_chat()

    check = Checkpoint(my_chat=my_chat, my_user=my_user)
    await check.check_documents()

    await message.answer(text=msg_texts[my_user.get_lang()]['start_msg'])


async def main():
    register_location_handler(dp)
    register_phone_handler(dp)
    register_new_member_handler(dp)
    register_join_req_handler(dp)
    dp.register_message_handler(start_hand, lambda message: message.text == '/start' and message.chat.type == 'private')
    dp.register_message_handler(start_hand_group, lambda message: message.text == '/start' and message.chat.type == 'group')
    print('starting..')
    await dp.start_polling(bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
