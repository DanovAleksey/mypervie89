
import telebot
from conf import tocen , textStart
from telebot import types

bot = telebot.TeleBot(tocen)

@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton('Общая инфа')
    # item2 = types.KeyboardButton('Мероприятия')
    # item3 = types.KeyboardButton('Участники')
    # item4 = types.KeyboardButton('Отделения')
    # item5 = types.KeyboardButton('Техвопросы')
    item6 = types.KeyboardButton('Помощь друга')
    markup1.add(item6)
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Общая инфа',url='https://ответы.будьвдвижении.рф/?group=dre')
    item2 = types.InlineKeyboardButton('Мероприятия',url='https://будьвдвижении.рф/projects')
    item3 = types.InlineKeyboardButton('Участники',url='https://ответы.будьвдвижении.рф/?group=abc')
    item4 = types.InlineKeyboardButton('Отделения',url='https://ответы.будьвдвижении.рф/?group=structure')
    item5 = types.InlineKeyboardButton('Техвопросы',url='https://ответы.будьвдвижении.рф/?group=tech')
    markup.add(item1,item2,item3,item4,item5)
    bot.send_message(message.chat.id, textStart , reply_markup= markup)
    bot.send_message(message.chat.id, 'Или подай заявку', reply_markup= markup1)




@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Помощь друга':
            # name = input('Укажи ФИО')
            msg = bot.send_message(message.chat.id,'Укажи ФИО')
            bot.register_next_step_handler(msg, namepolz )
            
            def namepolz(message):
                bot.send_message(message.chat.id, 'на предыдущем шаге вы ввели\n{}'.format(message.text))
            # let = float(input('Укажи сколько тебе лет'))
#             markup = types.InlineKeyboardMarkup()
#             item1 = types.InlineKeyboardButton('Общая инфа',url='https://ответы.будьвдвижении.рф/?group=dre')
#             markup.add(item1)
#             bot.send_message(message.chat.id, 'Нажми кнопку и перейди на сайт',reply_markup= markup)
#         elif message.text == 'Мероприятия':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Общая инфа')
#             # item2 = types.KeyboardButton('Участники')
#             # item3 = types.KeyboardButton('Отделения')
#             # item4 = types.KeyboardButton('Техвопросы')
#             # item5 = types.KeyboardButton('Помощь друга')
#             # back = types.KeyboardButton('Назад')
#             # markup.add(item1, item2, item3, item4, item5,back)
#             markup.add(item1)
#             bot.send_message(message.chat.id, 'Мероприятия', reply_markup= markup)
#         elif message.text == 'Участники':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Общая инфа')
#             # item2 = types.KeyboardButton('Мероприятия')
#             # item3 = types.KeyboardButton('Отделения')
#             # item4 = types.KeyboardButton('Техвопросы')
#             # item5 = types.KeyboardButton('Помощь друга')
#             # back = types.KeyboardButton('Назад')
#             # markup.add(item1, item2, item3, item4, item5,back)
#             markup.add(item1)
#             bot.send_message(message.chat.id, 'Участники', reply_markup= markup)
#         elif message.text == 'Отделения':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Общая инфа')
#             item2 = types.KeyboardButton('Мероприятия')
#             item3 = types.KeyboardButton('Участники')
#             item4 = types.KeyboardButton('Техвопросы')
#             # item5 = types.KeyboardButton('Помощь друга')
#             # back = types.KeyboardButton('Назад')
#             # markup.add(item1, item2, item3, item4, item5,back)
#             markup.add(item1, item2, item3, item4)
#             bot.send_message(message.chat.id, 'Отделения', reply_markup= markup)
#         elif message.text == 'Техвопросы':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Общая инфа')
#             item2 = types.KeyboardButton('Мероприятия')
#             item3 = types.KeyboardButton('Участники')
#             # item4 = types.KeyboardButton('Отделения')
#             # item5 = types.KeyboardButton('Помощь друга')
#             # back = types.KeyboardButton('Назад')
#             # markup.add(item1, item2, item3, item4, item5,back)
#             markup.add(item1, item2, item3)
#             bot.send_message(message.chat.id, 'Техвопросы', reply_markup= markup)
#         elif message.text == 'Назад':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Общая инфа')
#             item2 = types.KeyboardButton('Мероприятия')
#             # item3 = types.KeyboardButton('Участники')
#             # item4 = types.KeyboardButton('Отделения')
#             # item5 = types.KeyboardButton('Техвопросы')
#             # item6 = types.KeyboardButton('Помощь друга')
#             # markup.add(item1, item2, item3, item4, item5, item6)
#             markup.add(item1, item2)
#             bot.send_message(message.chat.id, 'Назад', reply_markup= markup)

bot.polling(none_stop=True)