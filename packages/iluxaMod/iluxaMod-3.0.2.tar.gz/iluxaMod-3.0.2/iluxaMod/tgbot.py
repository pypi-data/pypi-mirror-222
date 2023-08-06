

class tgBot:

    def __init__(self, token):
        import telebot
        self.token = token
        self.bot = telebot.TeleBot(self.token)

    def send(self, chat_id, msg, reply_markup=None, disable_notification=False):
        self.bot.send_message(chat_id, msg, reply_markup=reply_markup, disable_notification=disable_notification,
                         parse_mode='HTML')

    def kmarkup(self):
        from telebot import types

        return types.InlineKeyboardMarkup()

    def back(self, callback_data, bname="Back"):
        from telebot import types

        return types.InlineKeyboardButton(bname, callback_data=callback_data)

    def btn(self, button_id, callback_data=None, url=None):
        from telebot import types

        return types.InlineKeyboardButton(button_id, callback_data=callback_data, url=url)
