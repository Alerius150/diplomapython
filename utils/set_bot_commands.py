import telebot
from telebot.types import BotCommand
from config_data.my_config import DEFAULT_COMMANDS
from utils.logger import logger


def set_default_commands(bot: telebot) -> None:
    """
    Команды бота
    """
    logger.info(' ')
    try:
        bot.set_my_commands(
            [BotCommand(*i) for i in DEFAULT_COMMANDS]
        )
    except BaseException as e:
        logger.exception(e)