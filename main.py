# from tolgas import tolgasAPI
from telebot import TeleBot


def main() -> None:
    # запрос токена из файла token
    with open('token', 'r') as token:
        BOT_TOKEN = token.read()

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

    bot.polling()


if __name__ == '__main__':
    main()
