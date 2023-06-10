from checkpoints.location_check import register_location_handler
from checkpoints.phone_check import register_phone_handler
from updates_handling.new_chat_memb import register_new_member_handler
from aiogram import types
from keyboards import start_keyboard
from MyUser import MyUser
from run_bot import dp, bot
from texts import msg_texts
import asyncio


async def start_hand(message: types.Message):
    my_user = MyUser(user_id=message.from_user.id, user=message.from_user)
    await my_user.find_lang()
    await message.answer(text=msg_texts[my_user.get_lang()]['start_msg'], reply_markup=start_keyboard(my_user.get_lang()))


async def main():
    register_location_handler(dp)
    register_phone_handler(dp)
    register_new_member_handler(dp)
    dp.register_message_handler(start_hand, commands=['start'])
    print('starting..')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
