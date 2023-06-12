from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import start_keyboard, share_phone_keyboard
from run_db import USERS_TB
from MyUser import MyUser
from texts import is_but_text
import asyncio


class Phone(StatesGroup):
    user_id = State()
    chat_id = State()
    phone = State()


async def phone_but_hand(message: Message):
    my_user = MyUser(table=USERS_TB, user_id=message.from_user.id, user=message.from_user)
    await my_user.find_lang()

    await message.answer('Share your phone number', reply_markup=share_phone_keyboard(my_user.get_lang()))
    await Phone.phone.set()
    state: FSMContext = Dispatcher.get_current().current_state(chat=message.chat.id, user=message.from_user.id)
    await asyncio.sleep(300)
    await state.finish()


async def phone_hand(message: Message, state: FSMContext):
    my_user = MyUser(table=USERS_TB, user_id=message.from_user.id, user=message.from_user)
    await my_user.find_lang()

    if message.contact.user_id == message.from_user.id:
        await state.finish()
        await message.delete()

        my_user.set_phone_position(phone_number=message.contact.phone_number)
        country_code = await my_user.phone_position.find_country_code()

        await message.answer(f"{country_code}")

        if country_code not in ['RU']:
            await message.answer('Молодець, козаче!', reply_markup=start_keyboard(my_user.get_lang()))

    else:
        await message.answer("You have to send your contact")


def register_phone_handler(dp: Dispatcher):
    dp.register_message_handler(phone_but_hand, lambda message: is_but_text(message.text, ['phone']))
    dp.register_message_handler(phone_hand, content_types=['contact'], state=Phone.phone)
