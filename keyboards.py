import time

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat, InlineKeyboardButton
from texts import but_texts


def start_keyboard(lang: str):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(but_texts[lang]['location']))
    keyboard.add(KeyboardButton(but_texts[lang]['phone']))
    keyboard.add(KeyboardButton(but_texts[lang]['chat'],
                                request_chat=KeyboardButtonRequestChat(request_id=int(time.time()),
                                                                       chat_is_channel=False,
                                                                       bot_is_member=True)))
    return keyboard


def share_phone_keyboard(lang: str):
    share_phone_keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    share_phone_keyb.add(KeyboardButton(but_texts[lang]['send_phone'], request_contact=True))
    return share_phone_keyb
