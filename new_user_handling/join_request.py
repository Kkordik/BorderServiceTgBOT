from aiogram.types import Message, ChatJoinRequest
from aiogram import Dispatcher
from run_bot import dp, bot
from keyboards import start_keyboard, requirement_keyboard
from MyUser import MyUser
from MyChat import MyChat
from checkpoint.Checkpoint import Checkpoint
from run_db import USERS_TB, CHATS_TB
from texts import msg_texts


async def join_req(request: ChatJoinRequest):
    print("sddscdscd d sdsd ")
    my_user = MyUser(table=USERS_TB, user_id=request.from_user.id, user=request.from_user)
    await my_user.insert_user()
    await my_user.find_lang()

    my_chat = MyChat(table=CHATS_TB, chat_id=request.chat.id, chat=request.chat)
    await my_chat.insert_chat()

    check = Checkpoint(my_chat=my_chat, my_user=my_user)
    if await check.check_documents():
        await request.approve()
        await bot.send_message(chat_id=request.from_user.id,
                               text=msg_texts[my_user.get_lang()]['start_msg'],
                               reply_markup=start_keyboard(my_user.get_lang()))

    else:
        await my_chat.find_requirements()
        await bot.send_message(chat_id=request.from_user.id,
                               text=msg_texts[my_user.get_lang()]['have_to_approve'],
                               reply_markup=requirement_keyboard(lang=my_user.get_lang(),
                                                                 requirements_list=my_chat.requirements_list))


def register_join_req_handler(dp: Dispatcher):
    dp.register_chat_join_request_handler(join_req, lambda request: True)
