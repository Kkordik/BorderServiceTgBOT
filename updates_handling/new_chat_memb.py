from aiogram.types import Message, ContentType, ChatJoinRequest
from aiogram import Dispatcher
from run_bot import dp, bot
from keyboards import start_keyboard
from MyUser import MyUser
from texts import msg_texts


async def new_chat_member(message: Message):
    print(message.new_chat_members, message.chat.title)


async def join_req(request: ChatJoinRequest):
    my_user = MyUser(user_id=request.from_user.id, user=request.from_user)
    await my_user.find_lang()
    await bot.send_message(chat_id=request.from_user.id,
                           text=msg_texts[my_user.get_lang()]['start_msg'],
                           reply_markup=start_keyboard(my_user.get_lang()))


def register_new_member_handler(dp: Dispatcher):
    dp.register_chat_join_request_handler(join_req, lambda request: True)
    dp.register_message_handler(new_chat_member, content_types=ContentType.NEW_CHAT_MEMBERS)


