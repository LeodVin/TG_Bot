# from background import keep_alive
# import pip
# pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types

# Тело программы ниже

# bot = telebot.TeleBot('5370070931:AAHf-lY434h-UiHis9uz5PcSNzO2SM5FKh4') # бот Николай
bot = telebot.TeleBot('6013135310:AAHOlRh3uCIuykC7RKECU5qwXM0B3tundzM') # бот NikolaiBotUser
# bot = telebot.TeleBot('5883552470:AAFWa7VmRVZCpFdRWXRM7V7NGfeEQWDPln0') # бот Николай асситент

link = {
    'LR_9': 'https://physlab.itch.io/virtual-lab-9',
    'Otchet_LR_9': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/9_otchet.pdf',
    'Guide_LR_9': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/9.pdf',
    'Test_LR_9': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18969',
    'LR_7': 'https://physlab.itch.io/virtual-lab-7',
    'Otchet_LR_7': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/7_otchet.pdf',
    'Guide_LR_7': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/new/7.pdf',
    'Test_LR_7': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18970',
    'LR_16': 'https://physlab.itch.io/lab-16',
    'Otchet_LR_16': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/16_otchet.pdf',
    'Guide_LR_16': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/new/16.pdf',
    'Test_LR_16': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18971',
    'LR_28': 'https://physlab.itch.io/virtual-lab-28',
    'Otchet_LR_28': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/28_otchet.pdf',
    'Guide_LR_28': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/28.pdf',
    'Test_LR_28': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18972',
    'Part_1_IDZ_1': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18066',
    'Part_1_IDZ_2': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18067',
    'Part_1_KR': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18273',
    'Part_1_TK': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18080',
    'LR_15': 'https://physlab.itch.io/virtual-lab-15',
    'Otchet_LR_15': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/15_otchet.pdf',
    'Guide_LR_15': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/15.pdf',
    'Test_LR_15': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18715',
    'LR_17': 'https://physlab.itch.io/virtual-lab-17',
    'Otchet_LR_17': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/17_otchet.pdf',
    'Guide_LR_17': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/17.pdf',
    'Test_LR_17': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18716',
    'LR_26': 'https://physlab.itch.io/virtual-lab-26',
    'Otchet_LR_26': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/otchet/26_otchet.pdf',
    'Guide_LR_26': 'https://kf-info.urfu.ru/fileadmin/user_upload/site_62_6389/pdf/new/26.pdf',
    'Test_LR_26': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18955',
    'Part_2_IDZ': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18683',
    'Part_2_TK': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18973'
}

answer_1 = '''
Приветствую тебя должник!!!
Ты попал в телеграмм бот для должников, а это значит что ты не все сдал по курсу общей физики, что от тебя требовалосью
Если ты оказался здесь значит у тебся есть долг.
Здесь можно сдать долг по 1-й и 2-й части физики. Подсказка:
1-ю часть физики обычно проходят в первом семестре и включает следующие разделы:
- Механика;
- Термодинамика, молекулярная физика;
- Электростатика, постоянный ток;
- Магнетизм.
2-я часть физики обычно проходит во втором семестре и включает следующие разделы:
- Электромагнитные явления;
- Колебания и волны;
- Волновая оптика;
- Квантовая оптика;
- Элементы квантовой механики;
- Основы физики атомного ядра.
Для оказания помощи тебе необходимо определить по какой из частей у тебя долг. Если долг по первой части напиши в чат "1-я часть". Если долг по второй части, напиши в чат "2-я часть".
'''

answer_2 = '''
В первой части были следующие контрольные мероприятия:
- Лабораторная работа 9
- Лабораторная работа 10
- Лабораторная работа 16
- Лабораторная работа 28
- ИДЗ-1
- ИДЗ-2
- Коллоквиум
- Контрольная работа
'''

answer_3 = f"""
Выполните лабораторную работу по ссылке: {link['LR_9']}.
Методичка к ЛР по ссылке: {link['Guide_LR_9']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_9']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_9']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_4 = f"""
Выполните лабораторную работу по ссылке: {link['LR_7']}.
Методичка к ЛР по ссылке: {link['Guide_LR_7']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_7']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_7']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_5 = f"""
Выполните лабораторную работу по ссылке: {link['LR_16']}.
Методичка к ЛР по ссылке: {link['Guide_LR_16']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_16']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_16']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_6 = f"""
Выполните лабораторную работу по ссылке: {link['LR_28']}.
Методичка к ЛР по ссылке: {link['Guide_LR_28']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_28']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_28']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_7 = f"""
Выполните ИДЗ-1 по ссылке: {link['Part_1_IDZ_1']}.
После того как ИДЗ-1 будет выполненно свяжитесь с преподавателем для проставления оценки.
"""

answer_8 = f"""
Выполните ИДЗ-2 по ссылке: {link['Part_1_IDZ_2']}.
После того как ИДЗ-2 будет выполненно свяжитесь с преподавателем для проставления оценки.
"""

answer_9 = f"""
Выполните контрольную работу по ссылке: {link['Part_1_KR']}.
После того как КР будет выполненна свяжитесь с преподавателем для проставления оценки.
"""

answer_10 = f"""
Выполните коллоквиум по ссылке: {link['Part_1_TK']}.
После того как коллоквиум будет выполненн свяжитесь с преподавателем для проставления оценки.
"""

answer_11 = '''
Во второй части были следующие контрольные мероприятия:
- Лабораторная работа 15 или Лабораторная работа 17
- Лабораторная работа 26
- ИДЗ
- Коллоквиум
'''

answer_12 = f"""
Выполните лабораторную работу по ссылке: {link['LR_15']}.
Методичка к ЛР по ссылке: {link['Guide_LR_15']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_15']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_15']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_13 = f"""
Выполните лабораторную работу по ссылке: {link['LR_17']}.
Методичка к ЛР по ссылке: {link['Guide_LR_17']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_17']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_17']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_14 = f"""
Выполните лабораторную работу по ссылке: {link['LR_26']}.
Методичка к ЛР по ссылке: {link['Guide_LR_26']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_26']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_26']}.
После того как отчет будет заполнен и тест пройден свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_15 = f"""
Выполните ИДЗ по ссылке: {link['Part_2_IDZ']}.
После того как ИДЗ будет выполненно свяжитесь с преподавателем для проставления оценки.
"""

answer_16 = f"""
Выполните ИДЗ по ссылке: {link['Part_2_TK']}.
После того как коллоквиум будет выполненн свяжитесь с преподавателем для проставления оценки.
"""

answer_17 = f"""
Я тебя не понимаю. Напиши один из вариантов:
1-я часть
2-я часть
"""

answer_18 = f"""
Я тебя не понимаю. Напиши один из вариантов:
Лабораторная работа 9
Лабораторная работа 10
Лабораторная работа 16
Лабораторная работа 28
ИДЗ-1
ИДЗ-2
Коллоквиум
Контрольная работа
"""

answer_19 = f"""
Я тебя не понимаю. Напиши один из вариантов:
Лабораторная работа 15
Лабораторная работа 17
Лабораторная работа 26
ИДЗ
Коллоквиум
"""

# @bot.message_handler(commands=['start'])
# def get_command(message):
#     bot.send_message(message.from_user.id, answer_1)


class Main_dialog:

    bot = telebot.TeleBot('6013135310:AAHOlRh3uCIuykC7RKECU5qwXM0B3tundzM')  # бот NikolaiBotUser

    @bot.message_handler(content_types=['text'])
    def start(self, message, bot):
        if (message.text == "start" or
                message.text == "/start" or
                message.text == "Начало" or
                message.text == "Start" or
                message.text == "начало" or
                message.text == "/Start"):
        bot.send_message(message.from_user.id, answer_1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("1-я часть")
        btn2 = types.KeyboardButton("2-я часть")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         'Так по какой из частей физики у тебя долг (введи 1-я часть или 2-я часть?',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_part)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "start":
        bot.send_message(message.from_user.id, answer_1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1-я часть")
        btn2 = types.KeyboardButton("2-я часть")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         'Так по какой из частей физики у тебя долг (введи 1-я часть или 2-я часть?',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_part)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши start")
    # elif message.text == "1-я часть":
    #     bot.send_message(message.from_user.id, answer_2)
    #     if message.text == "Лабораторная работа №9":
    #         bot.send_message(message.from_user.id, answer_3)
    #     else:
    #         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")

def get_part(message):
    if message.text == "1-я часть":
        bot.send_message(message.from_user.id, answer_2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Лабораторная работа 9")
        btn2 = types.KeyboardButton("Лабораторная работа 10")
        btn3 = types.KeyboardButton("Лабораторная работа 16")
        btn4 = types.KeyboardButton("Лабораторная работа 28")
        btn5 = types.KeyboardButton("ИДЗ-1")
        btn6 = types.KeyboardButton("ИДЗ-2")
        btn7 = types.KeyboardButton("Коллоквиум")
        btn8 = types.KeyboardButton("Контрольная работа")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id,
                         'Что из вышеперечисленного вы хотели бы сдать (напишете один вариант)?',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_subject_1)
    elif message.text == "2-я часть":
        bot.send_message(message.from_user.id, answer_11)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Лабораторная работа 15")
        btn2 = types.KeyboardButton("Лабораторная работа 17")
        btn3 = types.KeyboardButton("Лабораторная работа 26")
        btn4 = types.KeyboardButton("ИДЗ")
        btn5 = types.KeyboardButton("Коллоквиум")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id,
                         'Что из вышеперечисленного вы хотели бы сдать (напишете один вариант)?',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_subject_2)
    # elif message.text == "2-я часть":
    #     bot.send_message(message.from_user.id, answer_45)
    #     bot.register_next_step_handler(message, get_subject)
    else:
        bot.send_message(message.from_user.id, answer_17)

def get_subject_1(message):
    if message.text == 'Лабораторная работа 9':
        bot.send_message(message.from_user.id, answer_3)
    elif message.text == 'Лабораторная работа 10':
        bot.send_message(message.from_user.id, 'Виртуальная ЛР №10 сейчас недоступна. Предлагаю пройти лабораторную работу №7')
        bot.send_message(message.from_user.id, answer_4)
    elif message.text == 'Лабораторная работа 16':
        bot.send_message(message.from_user.id, answer_5)
    elif message.text == 'Лабораторная работа 28':
        bot.send_message(message.from_user.id, answer_6)
    elif message.text == 'ИДЗ-1':
        bot.send_message(message.from_user.id, answer_7)
    elif message.text == 'ИДЗ-2':
        bot.send_message(message.from_user.id, answer_8)
    elif message.text == 'Контрольная работа':
        bot.send_message(message.from_user.id, answer_9)
    elif message.text == 'Коллоквиум':
        bot.send_message(message.from_user.id, answer_10)
    else:
        bot.send_message(message.from_user.id, answer_18)

def get_subject_2(message):
    if message.text == 'Лабораторная работа 15':
        bot.send_message(message.from_user.id, answer_12)
    elif message.text == 'Лабораторная работа 17':
        bot.send_message(message.from_user.id, answer_13)
    elif message.text == 'Лабораторная работа 26':
        bot.send_message(message.from_user.id, answer_14)
    elif message.text == 'ИДЗ':
        bot.send_message(message.from_user.id, answer_15)
    elif message.text == 'Коллоквиум':
        bot.send_message(message.from_user.id, answer_16)
    else:
        bot.send_message(message.from_user.id, answer_19)

# Тело программы выше


# keep_alive()
bot.polling(none_stop=True, interval=0)