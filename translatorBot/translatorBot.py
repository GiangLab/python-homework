
from ast import Import, Try
from os import name
#import sqlite3
import telebot
from telebot import types
from datetime import datetime
import config
import statFuncs
import recognizeText
import translatorText
from users import User


bot = telebot.TeleBot(config.TOKEN)
cur_dt = datetime.now()
botUser = User("Инкогнито", 0, f'{cur_dt.day}.{ cur_dt.month}.{cur_dt.year}', '', '', '', '')
  
@bot.message_handler(commands=['start'])
def start(message):
    global botUser
    
    #global user_id
    botUser.user_id = message.from_user.id;

    # ищем пользователя в таблице user с user_id и 
    # создаем базу данных для хранения информации о пользователе если она не существует
    #res=statisticsBot.userSearch(botUser.user_id)

    bot.send_message(message.chat.id, text="👋 Мы ради, что вы решили воспользоваться нашим чат-ботом ")
    botUser.name = message.text.strip()
    main_menu(message.chat.id)


def user_information(message):
    global botUser

    # сохраняем информацию по переводу
    botUser.user_id = message.from_user.id;
    statFuncs.add_data(botUser.user_id)
    main_menu(message.chat.id)

 
def main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Перевод текста")
    btn2 = types.KeyboardButton("👩🏻‍🏫 Разработчики")
    btn3 = types.KeyboardButton("📰 Статистика")
    markup.row(btn1)
    markup.row(btn2, btn3)
    #markup.add(btn1, btn2, , btn4)
    # bot.send_message(message.chat.id, text="👋 Здравствуйте, {0.first_name}! ".format(message.from_user), reply_markup=markup)
    bot.send_message(chat_id, f"👀 Выбери интересующий Вас раздел",parse_mode='html', reply_markup=markup)


def original(message):#После "перенаправления" функция сработает, лишь после получения message
    try:
        botUser.original = message.text.strip()
        info = f"Введенный текст:\n"
        info += f"<b> {botUser.original} </b>\n "
    except Exception:
        bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\n ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        bot.send_message(message.chat.id, f"Вернитесь в главное меню и попробуйт еще раз ",parse_mode='html', reply_markup=markup)
    else:
        # переводим текст
        if (botUser.directionOfTranslation == 'ru_en'):
            langTranslation="en"
        else:
            langTranslation="ru"
    
        textTranslate=translatorText.translate_text(botUser.original,langTranslation)
        if (textTranslate == '#4'):
            info = f"Ошибка текущего превода \n"
        else:
            info+= f'Перевод теста:\n'
            info += f"<b> {textTranslate} </b>\n "
            botUser.translation=textTranslate
            bot.send_message(message.chat.id,info,parse_mode='html')
            user_information(message) 


#def handle_img(message):
@bot.message_handler(content_types=['photo'])
def inputImg(message):
    try:
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = config.PATH_img
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception:
        bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\n ')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        bot.send_message(message.chat.id, f"Вернитесь в главное меню и попробуйт еще раз ",parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Изображение сохранено")
        recognizeImg(message)

def recognizeImg(message):
    global botUser

    # распознование текста с картинки
    src = config.PATH_img
    if (botUser.directionOfTranslation == 'ru_en'):
        language="rus"
        langTranslation="en"
        bot.send_message(message.chat.id, f"<i>распознование русского текста</i> ",parse_mode='html')
    else:   
        language="eng"
        langTranslation="ru"
        bot.send_message(message.chat.id, f"<i>распознование английского текста</i> ",parse_mode='html')

    textImg = recognizeText.recognize(src,language)
    if (textImg == '#0'):
       info = f"Файл не найден. Попробуйте еще раз.\n"
    elif (textImg == '#1'):
       info = f"Не удалось обработать изображение. Попробуйте еще раз\n"
    elif (textImg == '#2'):
       info = f"Ошибка распознавания текста. Попробуйте еще раз\n"
    elif (textImg == '#3'):
       info = f"Ошибка установки пути к Tesseract. Попробуйте еще раз\n"
    else: 
       info = f"Распознанный текст:\n"
       info += f"<b> {textImg} </b>\n "
       botUser.original=textImg
       # переводим текст
       textTranslate=translatorText.translate_text(textImg,langTranslation)
       if (textTranslate == '#4'):
           info = f"Ошибка текущего превода \n"
       else: 
           info+= f'Перевод теста:\n'
           info += f"<b> {textTranslate} </b>\n "
           botUser.translation=textTranslate
       bot.send_message(message.chat.id, info,parse_mode='html')
       user_information(message) 

@bot.message_handler(content_types=['text'])
def func(message):
    
    if(message.text == "Перевод текста"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Перевод с русского на английский")
        btn2 = types.KeyboardButton("Перевод с английского на русский")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(btn1)
        markup.row(btn2)
        markup.row(back)
        bot.send_message(message.chat.id, text="Выберите направление перевода", reply_markup=markup)
    elif((message.text == "Перевод с русского на английский") or (message.text == "Перевод с английского на русский")):
        if (message.text == "Перевод с русского на английский"):
           botUser.directionOfTranslation ='ru_en'
        else:   
           botUser.directionOfTranslation ='en_ru'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Разпознать текст")
        btn2 = types.KeyboardButton("Ввести текст")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(btn1, btn2)
        markup.row(back)
        bot.send_message(message.chat.id, f"Выберите способ ввода текста ",parse_mode='html', reply_markup=markup)
    elif(message.text == "Разпознать текст"):
        botUser.inputType = 'recognize'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        bot.send_message(message.chat.id, text="Загрузите изображение с текстом", reply_markup=markup)
        bot.register_next_step_handler(message, inputImg) #"Перенаправляет" на след.функцию
    elif(message.text == "Ввести текст"):
        botUser.inputType = 'input'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        bot.register_next_step_handler(message, original) #"Перенаправляет" на след.функцию
    elif(message.text == "👩🏻‍🏫 Разработчики"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        bot.send_message(message.chat.id, text="Телеграмм - бот разработали".format(message.from_user))
        bot.send_message(message.from_user.id, 'студенты группы 5130203/20102: \n\
                                                • Цвиркун Никита \n\
                                                • Максимов Иван \n\
                                                • Ха Хоанг Жанг \n\
                                                • Ващилко Алексей', reply_markup=markup)
    elif message.text == "📰 Статистика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Статистика по пользователям за текущий день")
        btn2 = types.KeyboardButton("Удаленние статистики")
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(btn1)
        markup.row(btn2)
        markup.row(back)
        bot.send_message(message.chat.id, text="Выберите вид отчета", reply_markup=markup)
    elif message.text == "Статистика по пользователям за текущий день":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        info = statFuncs.get_report(datetime.today().strftime('%Y-%m-%d'))
        bot.send_message(message.chat.id, info,parse_mode='html', reply_markup=markup)
    elif message.text == "Данные по пользователям за весь период":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        info = statFuncs.get_data()
        bot.send_message(message.chat.id, info,parse_mode='html', reply_markup=markup)
    elif message.text == "Удаленние статистики":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("🔙 Вернуться в главное меню")
        markup.row(back)
        info = statFuncs.flush_data()
        bot.send_message(message.chat.id, "stat",parse_mode='html', reply_markup=markup)
        #bot.send_message(message.chat.id, info,parse_mode='html', reply_markup=markup)
    elif (message.text == "🔙 Вернуться в главное меню"):
            main_menu(message.from_user.id)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


bot.polling(none_stop=True)

