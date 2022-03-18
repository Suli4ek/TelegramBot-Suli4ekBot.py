import telebot
import config
from telebot import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(config.API_TOKEN)

@bot.message_handler(commands=['start'])
def helloText(message):
    bot.send_message(message.chat.id, "Привет <b>{0.first_name}</b>!\nМеня зовут <u>{1.first_name}</u>, я пока ничего не умею, но я учусь и несомненно скоро стану очень умным ботом!\nДля того, чтобы узнать список доступных комманд, напиши мне в чат ""/help".format(message.from_user, bot.get_me()), parse_mode='html')
        
@bot.message_handler(commands=['help'])
def helpText (message):

    markup = types.InlineKeyboardMarkup(row_width=4)
    but1 = types.InlineKeyboardButton("Сободные даты", callback_data='Dates')
    but2 = types.InlineKeyboardButton("Контакты менеджеров", callback_data='Contacts')
    markup.add(but1, but2)
    
    bot.send_message(message.chat.id,"<b>Это раздел помощи.</b> \nВыбери нужную команду:", parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Dates':
                bot.send_message(call.message.chat.id, 'Эта часть еще не подключена к базе данных!')
            elif call.data == 'Contacts':
                bot.send_message(call.message.chat.id, '<b>Максим Пазеков</b>\nТелефон: +79372757719\n\nМенеджер <i>Pazekov Team</i>\nТелефон: +79372758875', parse_mode='html')
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Ваш запрос обработан!',
            reply_markup=None)
                
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, 
                text="Сулейман еще учится, пожалуйста, наберитесь терпения!")    

    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)
