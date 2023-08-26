import telebot
from telebot import types
from telebot.types import WebAppInfo
import json

bot = telebot.TeleBot('5874798151:AAG1Hr-YhsAfAdCQrtW2Af3m1nCwXNOhX34')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markupm = types.KeyboardButton('Сделать заказ', web_app=WebAppInfo(url='https://acseer.github.io/Botshop/'))
    markupk = types.KeyboardButton('Открыть канал с кроссовками', web_app=WebAppInfo(url='https://t.me/botshopa'))
    markupi = types.KeyboardButton('Информация')
    markuph = types.KeyboardButton('Помощь')
    markupp = types.KeyboardButton('Поддержать разаработчика')
    markup.add(markupm, markupk)
    markup.add(markupi, markuph)
    markup.add(markupp)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Информация':
        bot.send_message(message.chat.id, '<b>Информация о Боте</b>\
                                                В этом боте вы можете заказать нужные кроссовки, получить ссылку на канал с кроссовками, поддержать разработчика бота, получить информацию как произвести оплату и как работает магазин.',
                         parse_mode='html')

    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, '<b>Помощь в покупке</b>\
                                              Нажмите в главном меню на кнопку "Сделать заказ" там нажмите "Заказать", введите нужные данные, ждите когда с вами свяжутся.',
                         parse_mode='html')

    elif message.text == 'Поддержать разаработчика':
        bot.send_message(message.chat.id, 'Поддержать можно на карту: 2200 7008 9083 0580')
        bot.send_message(message.chat.id, '<b>Спасибо огромное, что решили поддержать нас!</b>', parse_mode='html')


    else:
        bot.send_message(message.chat.id, 'Извините, но я не знаю такой команды.')




@bot.message_handler(content_types="web_app_data") #получаем отправленные данные
def answer(webAppMes):
    res = json.loads(webAppMes.web_app_data.data)
    bot.send_message(webAppMes.chat.id, 'Благодорим за заказ! С вами скоро свяжется наш менеджер.')
    owner_chat_id = 1329365605  # Замените на ID вашего чата с ботом
    bot.send_message(owner_chat_id, f"Новая бронь: Name: {res['name']}. Email: {res['email']}. Phone: {res['phone']}. TGID: {res['tgid']} Cross: {res['cross']}")





bot.polling(none_stop=True)
