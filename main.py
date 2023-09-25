from datetime import datetime as dt
from tolgas import tolgasAPI
from telebot import TeleBot
from json import loads
import logging


def _log(reason: str, message=None) -> None:
    if message:
        log = {'userid':message.from_user.id, 'firstname': message.from_user.first_name, 'lastname': message.from_user.last_name, 'username': message.from_user.username, 'text':message.text}
    else:
        log = 'None'
    logging.info(f'{reason} :: {log}')
    print(f'{dt.now()} :: {reason} :: {log}')
"""
def timetableToText(timetable) -> str:
    result = ''
    #TODO:   next
    return result
"""
def main() -> None:
    with open('settings.json', 'r') as s:
        settings = loads(s.read())

    bot_token = settings['token']
    admin_id = settings['adminid']
    logging.basicConfig(level=logging.INFO, filename="logs.log", encoding='utf-8', format="%(asctime)s :: %(levelname)s :: %(message)s")
    tolgas = tolgasAPI()
    bot = TeleBot(bot_token)


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        _log('Новое сообщение', message)
        bot.send_message(message.from_user.id, "Бонжур! Я - неоффициальный бот, который помогает следить за расписанием Университета сервиса.\n\nДля более подробной информации: \n /help")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        _log('Новое сообщение', message)
        bot.send_message(message.from_user.id, "Бот в данный момент в разработке.\n\nСвязь с разработчиками: \n /send <Сообщение>")

    @bot.message_handler(commands=['today'])
    def send_timetable(message):
        _log('Новое сообщение', message)
        date = str(dt.now())[:10].split('-')
        date = f'{date[2]}.{date[1]}.{date[0]}'
        timetable = tolgas.getTimetable(groupid=0, fromdate=date, todate=date)
        #text = timetableToText(timetable)
        bot.send_message(message.from_user.id, str(timetable))

    @bot.message_handler(commands=['send'])
    def send_to_admin(message):
        _log('Новое сообщение', message)
        if message.text == '/send':
            bot.send_message(message.from_user.id, "Использование комманды:\n /send <Сообщение>")
        else:
            bot.send_message(admin_id, f'@{message.from_user.username}: {message.text[6:]}')

    @bot.message_handler(func=lambda message: True)
    def makelog(message):
        _log('Новое сообщение', message)

    _log('Новый запуск')
    bot.polling()


if __name__ == '__main__':
    main()
