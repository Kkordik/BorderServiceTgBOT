but_texts = {
    'uk': {
        'location': 'Перевірка через локацію',
        'phone': 'Перевірка через номер',
        'send_phone': 'Надіслати номер',
        'chat': 'Надіслати chat'
    },
    'en': {
        'location': 'Check by location',
        'phone': 'Check by phone number',
        'send_phone': 'Send phone number',
        'chat': 'Надіслати chat'
    }
}

inline_but_texts = {
    'uk': {

    },
    'en': {

    }
}

msg_texts = {
    'uk': {
        'start_msg': 'uk fuck russians',
        'new_chat_member': 'uk <a href="tg://user?id={}">{}</a>'

    },
    'en': {
        'start_msg': 'en fuck russians',
        'new_chat_member': 'en <a href="tg://user?id={}">{}</a>'
    }
}


def is_but_text(text: str, text_titles: list) -> bool:
    """
    Function to check if message text is KeyboardButton of specified titles
    :param text: message text
    :param text_titles: titles of KeyboardButtons to check
    :return: bool
    """
    for lang_texts in but_texts.values():
        for text_title in text_titles:
            if text == lang_texts[text_title]:
                return True
    return False

