from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from texts import but_texts


def start_keyboard(lang: str):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(but_texts[lang]['location']))
    keyboard.add(KeyboardButton(but_texts[lang]['phone']))
    return keyboard


def share_phone_keyboard(lang: str):
    share_phone_keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    share_phone_keyb.add(KeyboardButton(but_texts[lang]['send_phone'], request_contact=True))
    return share_phone_keyb
