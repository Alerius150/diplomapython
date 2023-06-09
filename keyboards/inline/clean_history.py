from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filter import for_history


def get_clean_button() -> InlineKeyboardMarkup:
    """
    Кнопка очистки истории
    :return: Кнопка очистки
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Очистить историю', callback_data=for_history.new(clean='Очистить')))
    return keyboard