# import pip
from background import keep_alive
# pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types
import tg_analytic

print('Hello world')

# bot = telebot.TeleBot('5370070931:AAHf-lY434h-UiHis9uz5PcSNzO2SM5FKh4') # бот Николай
# bot = telebot.TeleBot('6013135310:AAHOlRh3uCIuykC7RKECU5qwXM0B3tundzM') # бот NikolaiBotUser
bot = telebot.TeleBot('5883552470:AAFWa7VmRVZCpFdRWXRM7V7NGfeEQWDPln0') # бот Bot1

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
    'Part_2_TK': 'https://exam1.urfu.ru/mod/quiz/view.php?id=18973',
    'Part_1_Guide': 'https://elar.urfu.ru/bitstream/10995/40620/1/978-5-7996-1701-1_2016.pdf',
    'Part_2_Guide': 'https://elar.urfu.ru/bitstream/10995/46980/1/978-5-7996-1948-0_2017.pdf'
}

answer_1 = '''
Приветствую тебя должник!!!
Ты попал в чат-бот для должников, а это значит что ты не все сдал по курсу физики.
Здесь можно сдать долг по 1-й и 2-й части физики.
Подсказка:
1-ю часть физики обычно проходят в первом семестре и она включает следующие разделы:
- Механика;
- Термодинамика, молекулярная физика;
- Электростатика, постоянный ток;
- Магнетизм.
2-ю часть физики обычно проходят во втором семестре и она включает следующие разделы:
- Электромагнитные явления;
- Колебания и волны;
- Волновая оптика;
- Квантовая оптика;
- Элементы квантовой механики;
- Основы физики атомного ядра.
Для закрытия задолженности, тебе необходимо определить по какой из частей у тебя долг. Если долг по первой части напиши в чат "1-я часть". Если долг по второй части, напиши в чат "2-я часть".
'''

answer_2 = '''
В первой части были следующие контрольные мероприятия:
- Лабораторная работа 9;
- Лабораторная работа 10;
- Лабораторная работа 16;
- Лабораторная работа 28;
- ИДЗ-1;
- ИДЗ-2;
- Коллоквиум;
- Контрольная работа.
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
После того как отчет будет заполнен и тест пройден, свяжитесь с преподавателем для сдачи отчета по ЛР.
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
После того как ИДЗ-1 будет выполненно, свяжитесь с преподавателем для проставления оценки.
"""

answer_8 = f"""
Выполните ИДЗ-2 по ссылке: {link['Part_1_IDZ_2']}.
После того как ИДЗ-2 будет выполненно, свяжитесь с преподавателем для проставления оценки.
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
После того как отчет будет заполнен и тест пройден, свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_13 = f"""
Выполните лабораторную работу по ссылке: {link['LR_17']}.
Методичка к ЛР по ссылке: {link['Guide_LR_17']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_17']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_17']}.
После того как отчет будет заполнен и тест пройден, свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_14 = f"""
Выполните лабораторную работу по ссылке: {link['LR_26']}.
Методичка к ЛР по ссылке: {link['Guide_LR_26']}.
Заполните отчет. Заготовку отчета можно скачать по ссылке: {link['Otchet_LR_26']}.
Пройдите тест по ЛР по ссылке: {link['Test_LR_26']}.
После того как отчет будет заполнен и тест пройден, свяжитесь с преподавателем для сдачи отчета по ЛР.
"""

answer_15 = f"""
Выполните ИДЗ по ссылке: {link['Part_2_IDZ']}.
После того как ИДЗ будет выполненно свяжитесь с преподавателем для проставления оценки.
"""

answer_16 = f"""
Выполните коллоквиум по ссылке: {link['Part_2_TK']}.
После того как коллоквиум будет выполнен, свяжитесь с преподавателем для проставления оценки.
"""

answer_17 = f"""
Я тебя не понимаю. Напиши один из вариантов:
1-я часть;
2-я часть.
"""

answer_18 = f"""
Я тебя не понимаю. Напиши один из вариантов:
Лабораторная работа 9;
Лабораторная работа 10;
Лабораторная работа 16;
Лабораторная работа 28;
ИДЗ-1;
ИДЗ-2;
Коллоквиум;
Контрольная работа.
"""

answer_19 = f"""
Я тебя не понимаю. Напиши один из вариантов:
Лабораторная работа 15;
Лабораторная работа 17;
Лабораторная работа 26;
ИДЗ;
Коллоквиум.
"""

answer_20 = f"Для освоения материала по 1-й части физики будет полезно ознакомится с пособием по ссылке: {link['Part_1_Guide']}"

answer_21 = f"Для освоения материала по 2-й части физики будет полезно ознакомится с пособием по ссылке: {link['Part_2_Guide']}"

rul_1 = '<strong><em>ВНИМАНИЕ: Для закрытия долга, после того как будет выполнена работа, необходимо подключится к консультации. Консультации проходят по расписанию в команде в teams.</em></strong>'

rul_2 = '<strong><em>ВНИМАНИЕ: Для того, чтобы преподаватель зачел сданный долг, будьте готовы на консультации ответить на вопросы преподавателя по темам проделанной работы.</em></strong>'

rul_3 = '<strong><em>ВНИМАНИЕ: Необходимо вести запись ваших действии в процессе выполнения виртуальной ЛР, при этом на экране должно присутствовать окно с фронтальной камерой вашего устройства.</em></strong>'

# @bot.message_handler(commands=['start'])
# def get_command(message):
#     bot.send_message(message.from_user.id, answer_1)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    tg_analytic.statistics(message.chat.id, message.text)
    if message.text == "start" or message.text == "Start" or message.text == "/Start" or message.text == "/start":
        bot.send_message(message.from_user.id, answer_1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1-я часть")
        btn2 = types.KeyboardButton("2-я часть")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id,
                         'Так по какой из частей физики у тебя долг (введи 1-я часть или 2-я часть)?',
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_part)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для того, чтобы начать общение введи start")
    # elif message.text == "1-я часть":
    #     bot.send_message(message.from_user.id, answer_2)
    #     if message.text == "Лабораторная работа №9":
    #         bot.send_message(message.from_user.id, answer_3)
    #     else:
    #         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши start")
    elif message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st, message.chat.id)
            with open('%s.txt' % message.chat.id, 'r', encoding='utf-8') as file:
                bot.send_document(message.chat.id, file)
                tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st, message.chat.id)
            bot.send_message(message.chat.id, messages)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")

def get_part(message):
    tg_analytic.statistics(message.chat.id, message.text)
    if message.text != 'exit':
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("1-я часть")
        # btn2 = types.KeyboardButton("2-я часть")
        # markup.add(btn1, btn2)
        # bot.send_message(message.from_user.id,
        #                  '(введи 1-я часть или 2-я часть)',
        #                  reply_markup=markup)
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
                             'Что из вышеперечисленного вы хотели бы сдать (напишите один вариант)?',
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
                             'Что из вышеперечисленного вы хотели бы сдать (напишите один вариант)?',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_subject_2)
        # elif message.text == "2-я часть":
        #     bot.send_message(message.from_user.id, answer_45)
        #     bot.register_next_step_handler(message, get_subject)

        else:
            bot.send_message(message.from_user.id, answer_17)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1-я часть")
            btn2 = types.KeyboardButton("2-я часть")
            btn3 = types.KeyboardButton("exit")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id,
                             'Для выхода в начало диалога введи exit',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_part)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("start")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Для того, чтобы начать общение введи start", reply_markup=markup)

def get_subject_1(message):
    tg_analytic.statistics(message.chat.id, message.text)
    if message.text != 'exit':
        if message.text == 'Лабораторная работа 9':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_3, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'Лабораторная работа 10':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'Виртуальная ЛР №10 сейчас недоступна. Предлагаю пройти лабораторную работу №7')
            bot.send_message(message.from_user.id, answer_4, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'Лабораторная работа 16':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_5, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'Лабораторная работа 28':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_6, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'ИДЗ-1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_7, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        elif message.text == 'ИДЗ-2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_8, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        elif message.text == 'Контрольная работа':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_9, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        elif message.text == 'Коллоквиум':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_10, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_20)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        else:
            bot.send_message(message.from_user.id, answer_18)
            bot.send_message(message.from_user.id, 'Для выхода в начало диалога введи exit')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Лабораторная работа 9")
            btn2 = types.KeyboardButton("Лабораторная работа 10")
            btn3 = types.KeyboardButton("Лабораторная работа 16")
            btn4 = types.KeyboardButton("Лабораторная работа 28")
            btn5 = types.KeyboardButton("ИДЗ-1")
            btn6 = types.KeyboardButton("ИДЗ-2")
            btn7 = types.KeyboardButton("Коллоквиум")
            btn8 = types.KeyboardButton("Контрольная работа")
            btn9 = types.KeyboardButton("exit")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
            bot.send_message(message.from_user.id,
                             'Что из вышеперечисленного вы хотели бы сдать (напишете один вариант)?',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_subject_1)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("start")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Для того, чтобы начать общение введи start", reply_markup=markup)

def get_subject_2(message):
    tg_analytic.statistics(message.chat.id, message.text)
    if message.text != 'exit':
        if message.text == 'Лабораторная работа 15':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_12, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_21)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'Лабораторная работа 17':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_13, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_21)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'Лабораторная работа 26':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_14, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_21)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_3, parse_mode='HTML')
        elif message.text == 'ИДЗ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_15, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_21)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        elif message.text == 'Коллоквиум':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("start")
            markup.add(btn1)
            bot.send_message(message.from_user.id, answer_16, reply_markup=markup)
            bot.send_message(message.from_user.id, answer_21)
            bot.send_message(message.from_user.id, rul_1, parse_mode='HTML')
            bot.send_message(message.from_user.id, rul_2, parse_mode='HTML')
        else:
            bot.send_message(message.from_user.id, answer_19)
            bot.send_message(message.from_user.id, 'Для выхода в начало диалога введи exit')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Лабораторная работа 15")
            btn2 = types.KeyboardButton("Лабораторная работа 17")
            btn3 = types.KeyboardButton("Лабораторная работа 26")
            btn4 = types.KeyboardButton("ИДЗ")
            btn5 = types.KeyboardButton("Коллоквиум")
            btn6 = types.KeyboardButton("exit")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.from_user.id,
                             'Что из вышеперечисленного вы хотели бы сдать (напишете один вариант)?',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_subject_2)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("start")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Для того, чтобы начать общение введи start", reply_markup=markup)


keep_alive()
bot.polling(none_stop=True, interval=1)
