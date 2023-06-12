from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from texts import is_but_text
from MyUser import MyUser
from keyboards import start_keyboard
from run_db import USERS_TB
import asyncio


class Location(StatesGroup):
    user_id = State()
    chat_id = State()
    location = State()


async def location_but_hand(message: Message):
    await message.answer('Send the location, share it for 15+ min')
    await Location.location.set()
    state: FSMContext = Dispatcher.get_current().current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(user_id=message.from_user.id, chat_id=message.chat.id)
    await asyncio.sleep(300)
    await state.finish()


async def location_hand(message: Message, state: FSMContext):
    data = await state.get_data()

    my_user = MyUser(table=USERS_TB, user_id=message.from_user.id, user=message.from_user)
    await my_user.find_lang()

    if message.location.live_period and not message.is_forward() and\
            message.from_user.id == data['user_id'] and not message.via_bot:

        await state.finish()
        await message.delete()

        my_user.set_geo_position(latitude=message.location.latitude, longitude=message.location.longitude)
        country_code = await my_user.geo_position.find_country_code()
        await my_user.insert_geo_country_code(country_code)

        await message.answer(f"{my_user.geo_position.get_country_code()}")

        if my_user.geo_position.get_country_code() != 'RU':
            await message.answer('Молодець, козаче!', reply_markup=start_keyboard(my_user.get_lang()))

    else:
        await message.answer("You have to send live location")


def register_location_handler(dp: Dispatcher):
    dp.register_message_handler(location_but_hand, lambda message: is_but_text(message.text, ['location']))
    dp.register_message_handler(location_hand, content_types=['location'], state=Location.location)
