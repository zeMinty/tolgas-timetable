from datetime import datetime as dt
# from tolgas import tolgasAPI
from telebot import TeleBot
import logging


def _log(reason: str, message=None):
    logging.info(f'Reason:{reason}; Message:{message}')
    print(f'{dt.now()} ~ new log')


def main() -> None:
    # запрос токена из файла token
    with open('token', 'r') as token:
        BOT_TOKEN = token.read()

    # инициализации
    logging.basicConfig(filename="logs.log",
                        format="%(asctime)s - %(levelname)s: %(message)s")
    # tolgas = tolgasAPI()
    bot = TeleBot(BOT_TOKEN)

    # print(tolgas.getTimetable(groupid=0, fromdate='02.10.2023', todate='08.10.2023'))

    # обработчики
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Бонжур! Я - неоффициальный бот, который помогает следить за расписанием Университета сервиса.\n\nДля более подробной информации:\n/help")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(
            message, "Бот в данный момент в разработке.\nСвязь с разработчиком: @Xpymka890")

    @bot.message_handler(func=lambda message: True)
    def makelog(message):
        _log('Новое сообщение', message)

    _log('Новый запуск')
    bot.polling()


if __name__ == '__main__':
    main()
