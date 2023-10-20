import telebot
from telebot import types
import conf
import requests
import flask
import sqlite3
import pandas as pd

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)
bot.delete_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, " + message.from_user.first_name + "!")
    bot.send_message(message.chat.id, 'Этот бот поможет тебе хорошо провести время в Нижнем Новгороде!')
    menu1(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "button1":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Сормовский район", callback_data="button3")
        button2 = types.InlineKeyboardButton(text="Московский район", callback_data="button4")
        button3 = types.InlineKeyboardButton(text="Канавинский район", callback_data="button5")
        button4 = types.InlineKeyboardButton(text="Приокский район", callback_data="button6")
        button5 = types.InlineKeyboardButton(text="Ленинский район", callback_data="button7")
        button6 = types.InlineKeyboardButton(text="Автозаводский район", callback_data="button8")
        button7 = types.InlineKeyboardButton(text="Нижегородский район", callback_data="button9")
        button8 = types.InlineKeyboardButton(text="Советский район", callback_data="button10")
        button9 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        keyboard.add(button6)
        keyboard.add(button7)
        keyboard.add(button8)
        keyboard.add(button9)

        bot.send_message(call.message.chat.id, "Какой район тебе интересен?", reply_markup=keyboard)

    elif call.data == "button2":
        bot.send_message(call.message.chat.id, "Этот бот расскажет тебе о лучших ресторанах, театрах, музеях, ТЦ, парках и достопримечательностях в каждом из районов Нижнего Новгорода.")
        bot.send_message(call.message.chat.id, "Просто нажми кнопку 'Давай начнём!' и выбери интересный тебе район!")

        menu1(call.message)

    elif call.data == "button3":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button12")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button13")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Сормовском районе?", reply_markup=keyboard)

    elif call.data == "button4":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button14")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button15")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Московском районе?", reply_markup=keyboard)

    elif call.data == "button5":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button16")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button17")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Канавинском районе?", reply_markup=keyboard)

    elif call.data == "button6":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button18")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button19")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Приокском районе?", reply_markup=keyboard)

    elif call.data == "button7":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button20")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button21")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Ленинском районе?", reply_markup=keyboard)

    elif call.data == "button8":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button22")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button23")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Автозаводском районе?", reply_markup=keyboard)

    elif call.data == "button9":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button24")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button25")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Нижегородском районе?", reply_markup=keyboard)

    elif call.data == "button10":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Где бы поесть?", callback_data="button26")
        button2 = types.InlineKeyboardButton(text="Где бы культурно отдохнуть?", callback_data="button27")
        button3 = types.InlineKeyboardButton(text="В меню", callback_data="button11")

        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)

        bot.send_message(call.message.chat.id, "Отлично!")
        bot.send_message(call.message.chat.id, "Что конкретно тебя интересует в Советском районе?", reply_markup=keyboard)

    elif call.data == "button12":
        results(call.message, "Сормовский", "Где поесть")
        menu2(call.message)

    elif call.data == "button13":
        results(call.message, "Сормовский", "Культура")
        menu2(call.message)

    elif call.data == "button14":
        results(call.message, "Московский", "Где поесть")
        menu2(call.message)

    elif call.data == "button15":
        results(call.message, "Московский", "Культура")
        menu2(call.message)

    elif call.data == "button16":
        results(call.message, "Канавинский", "Где поесть")
        menu2(call.message)

    elif call.data == "button17":
        results(call.message, "Канавинский", "Культура")
        menu2(call.message)

    elif call.data == "button18":
        results(call.message, "Приокский", "Где поесть")
        menu2(call.message)

    elif call.data == "button19":
        results(call.message, "Приокский", "Культура")
        menu2(call.message)

    elif call.data == "button20":
        results(call.message, "Ленинский", "Где поесть")
        menu2(call.message)

    elif call.data == "button21":
        results(call.message, "Ленинский", "Культура")
        menu2(call.message)

    elif call.data == "button22":
        results(call.message, "Автозаводский", "Где поесть")
        menu2(call.message)

    elif call.data == "button23":
        results(call.message, "Автозаводский", "Культура")
        menu2(call.message)

    elif call.data == "button24":
        results(call.message, "Нижегородский", "Где поесть")
        menu2(call.message)

    elif call.data == "button25":
        results(call.message, "Нижегородский", "Культура")
        menu2(call.message)

    elif call.data == "button26":
        results(call.message, "Советский", "Где поесть")
        menu2(call.message)

    elif call.data == "button27":
        results(call.message, "Советский", "Культура")
        menu2(call.message)

    elif call.data == "button11":
        menu2(call.message)


def menu1(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Давай начнём!", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Что умеет этот бот?", callback_data="button2")

    keyboard.add(button1)
    keyboard.add(button2)

    bot.send_message(message.chat.id, "Начнём (нажми нужную кнопку)?", reply_markup=keyboard)


def menu2(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Хочу!", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Напомни-ка, что умеет этот бот?", callback_data="button2")

    keyboard.add(button1)
    keyboard.add(button2)

    bot.send_message(message.chat.id, "Хочешь узнать ещё больше интересных мест (нажми нужную кнопку)?", reply_markup=keyboard)


def results(message, district, type):
    conn = sqlite3.connect('NN_bot.db')
    cur = conn.cursor()
    query = '''
    SELECT place.name, place.description, place.open_hours, place.location, place.rating, place.reviews, place.picture FROM place
    JOIN place_district ON place.id = place_district.id_place
    JOIN district ON place_district.id_district = district.id
    JOIN place_type ON place.id = place_type.id_place
    JOIN type ON place_type.id_type = type.id
    WHERE district.name = '{district}'
    AND type.name = '{type}'
    '''.format(district=district, type=type)
    df_query = pd.read_sql_query(query, con=conn)
    conn.close()
    bot.send_message(message.chat.id, "Результаты для выбранного района:")
    for index, row in df_query.iterrows():
        bot.send_message(message.chat.id, f"Название: {row['name']}\nРейтинг: {row['rating']}\nЧасы работы: {row['open_hours']}\nРасположение: {row['location']}\n[Ссылка на отзывы]({row['reviews']})\nОписание: {row['description']}\nФото: {row['picture']}", parse_mode='Markdown')


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
