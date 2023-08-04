import logging
import time
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CallbackQueryHandler

logger = logging.getLogger(__name__)
countable = {}
count = {}
count_prez = {}
but_1 = InlineKeyboardButton("Назад", callback_data="Назад")
but_2 = InlineKeyboardButton('Вперёд', callback_data="Вперёд")
but_3 = InlineKeyboardButton('Выйти из презентации', callback_data="Выйти из презентации")
keyboard_full = InlineKeyboardMarkup([[but_1, but_2], [but_3]])
keyboard_start = InlineKeyboardMarkup([[but_2], [but_3]])
keyboard_end = InlineKeyboardMarkup([[but_1], [but_3]])
but1 = KeyboardButton('Проверить свои знания')
but2 = KeyboardButton('Презентация')
keyboard_0 = ReplyKeyboardMarkup([[but1], [but2]], one_time_keyboard=True)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global count
    global countable
    global count_prez
    if update.callback_query is not None:
        update.callback_query.answer()
        message = update.callback_query.message
        message_text = update.callback_query.data
    else:
        message = update.message
        message_text = message.text
    username = update.effective_user.username
    if(message_text == "/start"):
        count_prez[username] = 0
        count[username] = 0
        countable[username] = 0
        await message.reply_text("Вас приветсвует бот от компании лукойл 😀",reply_markup=keyboard_0)
    elif(message_text=='Проверить свои знания'):
        #but_1 = InlineKeyboardButton("Назад", callback_data="Назад")
        but11 = InlineKeyboardButton('Добычей нефти и газа',callback_data="Добычей нефти и газа")
        but22 = InlineKeyboardButton('Покупкой нефти и газа',callback_data="Покупкой нефти и газа")
        but33 = InlineKeyboardButton('Веб-дизайном', callback_data="Веб-дизайном")
        keyboard1 = InlineKeyboardMarkup([[but11], [but22], [but33]])
        await message.reply_photo("https://avatars.mds.yandex.net/i?id=04f34f9bb4609414ca491a3130d6b2b9aeedc22e-9083123-images-thumbs&n=13", "1.   Чем занимается компания “Лукойл”?", reply_markup=keyboard1)
        countable[username] = 1
    elif(countable[username] == 1):
        # check answer
        count[username] = 0
        if message_text == "Добычей нефти и газа":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username]+=1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but2_1 = InlineKeyboardButton('В 10', callback_data='В 10')
        but2_2 = InlineKeyboardButton('В 25', callback_data='В 25')
        but2_3 = InlineKeyboardButton('В 30', callback_data='В 30')
        keyboard3 = InlineKeyboardMarkup([[but2_1, but2_2, but2_3]])
        await message.reply_photo("https://static.tildacdn.com/tild3230-3466-4163-a532-326536373531/---.jpg", "2.	В скольких странах мира Лукойл занимается добычей и разведкой?", reply_markup=keyboard3)
        # countable
        countable[username] += 1
    elif (countable[username] == 2):
        # check answer
        if message_text == "В 30":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but3_1 = InlineKeyboardButton('19.000', callback_data='19.000')
        but3_2 = InlineKeyboardButton('Примерно 38.000', callback_data='Примерно 38.000')
        but3_3 = InlineKeyboardButton('Порядка 30.000', callback_data='Порядка 30.000')
        keyboard4 = InlineKeyboardMarkup([[but3_1], [but3_2], [but3_3]])
        await message.reply_photo(
            "https://enkistroy.ru/800/600/https/elektroportal.ru/wp-content/uploads/2020/09/592132.jpg",
            "3.	Сколько нефтедобывающих скважин в арсенале Лукойла?", reply_markup=keyboard4)
        # countable
        countable[username] += 1
    elif (countable[username] == 3):
        # check answer
        if message_text == "Порядка 30.000":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but4_1 = InlineKeyboardButton('Лазаревское, Углич, Киржач', callback_data='Лазаревское, Углич, Киржач')
        but4_2 = InlineKeyboardButton('Лангепас, Урай, Когалым', callback_data='Лангепас, Урай, Когалым')
        but4_3 = InlineKeyboardButton('Лабинск, Улейма, Кашпир', callback_data='Лабинск, Улейма, Кашпир')
        keyboard5 = InlineKeyboardMarkup([[but4_1], [but4_2], [but4_3]])
        await message.reply_photo(
            "https://avatars.mds.yandex.net/i?id=79b8b42bd72a1639f030b75c5728b8395d82146b-8979882-images-thumbs&n=13",
            "4.	От первых букв названия каких городов происходит ЛУК в названии Лукойл?", reply_markup=keyboard5)
        # countable
        countable[username] += 1
    elif (countable[username] == 4):
        # check answer
        if message_text == "Лангепас, Урай, Когалым":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but5_1 = InlineKeyboardButton('100.000', callback_data="100.000")
        but5_2 = InlineKeyboardButton('80.000', callback_data="80.000")
        but5_3 = InlineKeyboardButton('160.000', callback_data="160.000")
        keyboard6 = InlineKeyboardMarkup([[but5_1, but5_2, but5_3]])
        await message.reply_photo(
            "https://avatars.mds.yandex.net/i?id=aa041aa39e13f048da442737c1ed59ce45fbfab2-9231384-images-thumbs&n=13",
            "5.	Сколько человек включает в себя штат компании?", reply_markup=keyboard6)
        # countable
        countable[username] += 1
    elif (countable[username] == 5):
        # check answer
        if message_text == "100.000":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but6_1 = InlineKeyboardButton('56', callback_data='56')
        but6_2 = InlineKeyboardButton('63', callback_data='63')
        but6_3 = InlineKeyboardButton('60', callback_data='60')
        keyboard7 = InlineKeyboardMarkup([[but6_1, but6_2, but6_3]])
        await message.reply_photo(
            "https://sun6-20.userapi.com/Op5R4nZs0l_DeFF1LfoxNT_kt2npAamgwFTGRQ/_RptAzv5uzA.jpg",
            "6.	В скольких регионах России Лукойл ведёт работу?", reply_markup=keyboard7)
        # countable
        countable[username] += 1
    elif (countable[username] == 6):
        # check answer
        if message_text == "63":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but7_1 = InlineKeyboardButton('15%', callback_data='15%')
        but7_2 = InlineKeyboardButton('30%', callback_data='30%')
        but7_3 = InlineKeyboardButton('20%', callback_data='20%')
        keyboard8 = InlineKeyboardMarkup([[but7_1, but7_2, but7_3]])
        await message.reply_photo(
            "https://avatars.mds.yandex.net/i?id=295f0d7fe567217b717077f99052e38eb7d65e03-9123766-images-thumbs&n=13",
            "7.	Сколько процентов битумов в России выпускает Лукойл?", reply_markup=keyboard8)
        # countable
        countable[username] += 1
    elif (countable[username] == 7):
        # check answer
        if message_text == "20%":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but8_1 = InlineKeyboardButton('10 млрд', callback_data='10 млрд')
        but8_2 = InlineKeyboardButton('28 млрд', callback_data='28 млрд')
        but8_3 = InlineKeyboardButton('Более 35 млрд', callback_data='Более 35 млрд')
        keyboard9 = InlineKeyboardMarkup([[but8_1, but8_2, but8_3]])
        await message.reply_photo(
            "https://avatars.mds.yandex.net/i?id=193fdf7098be194421c7d713f78663a11a6cf30b-9042494-images-thumbs&n=13",
            "8.	Сколько денег в 2019 году Компания направила на охрану окружающей среды?", reply_markup=keyboard9)
        # countable
        countable[username] += 1
    elif (countable[username] == 8):
        # check answer
        if message_text == "Более 35 млрд":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but9_1 = InlineKeyboardButton('Более 90 млн тонн', callback_data='Более 90 млн тонн')
        but9_2 = InlineKeyboardButton('65 млн тонн', callback_data='65 млн тонн')
        but9_3 = InlineKeyboardButton('Порядка 80 млн тонн', callback_data='Порядка 80 млн тонн')
        keyboard10 = InlineKeyboardMarkup([[but9_1], [but9_2], [but9_3]])
        await message.reply_photo(
            "https://avatars.mds.yandex.net/i?id=79b8b42bd72a1639f030b75c5728b8395d82146b-8979882-images-thumbs&n=13",
            "9.	Сколько составляет ежегодная добыча нефти и газового конденсата ЛУКОЙЛа ", reply_markup=keyboard10)
        # countable
        countable[username] += 1
    elif (countable[username] == 9):
        # check answer
        if message_text == "Порядка 80 млн тонн":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        # new question
        but10_1 = InlineKeyboardButton('8', callback_data='8')
        but11_2 = InlineKeyboardButton('10', callback_data='10')
        but12_3 = InlineKeyboardButton('15', callback_data='15')
        keyboard11 = InlineKeyboardMarkup([[but10_1, but11_2, but12_3]])
        await message.reply_photo(
            "https://im.kommersant.ru/ISSUES.PHOTO/WEEKLY/2016/046/vzdr.png",
            "10.	Сколько месторождений Лукойл открыл в российском секторе Каспийского моря?", reply_markup=keyboard11)
        # countable
        countable[username] += 1
    elif (countable[username] == 10):
        # check answer
        if message_text == "10":
            time.sleep(0.5)
            await message.reply_text("Верно👌")
            time.sleep(0.5)
            count[username] += 1
        else:
            time.sleep(0.5)
            await message.reply_text("Неверно😢")
            time.sleep(0.5)
        But1 = KeyboardButton('Проверить свои знания')
        But2 = KeyboardButton('Презентация')
        keyboardAg = ReplyKeyboardMarkup([[But1], [But2]])
        await message.reply_text("Вы прошли тест!", reply_markup=keyboardAg)
        await message.reply_photo(
            "https://fikiwiki.com/uploads/posts/2022-02/1644725019_24-fikiwiki-com-p-yunost-krasivie-kartinki-28.jpg",
            "")
        await message.reply_text("Идёт подсчёт правильных ответов🤔")
        time.sleep(2)
        if(count[username]>=8):
            await message.reply_text("Поздравляю у вас "+str(count[username])+" баллов")
            await message.reply_text("За такой хороший результат вам положена награда)❤")
            time.sleep(2)
            await message.reply_text("http://t.me/addstickers/lukoil_stickers_by_fStikBot")
            await message.reply_text("Это ссылка на наш стикер пак😍")
        else:
            await message.reply_text("Поздравляю у вас " + str(count[username]) + " баллов")
            await message.reply_text("У вас не получилось набрать нужное количество баллов(😭")
            time.sleep(1)
            await message.reply_text("Попробуйте снова")
        countable[username] = -1
        count[username] = 0
    elif(message_text == "Презентация"):
        await message.reply_photo(
            "https://ibb.co/JqjWQnN",
            "",
            reply_markup=keyboard_start)
        count_prez[username] = 1
    elif (count_prez[username] == 1):
        if(message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/bHn466s",
                "",
                reply_markup=keyboard_full)
        elif(message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")


    elif (count_prez[username] == 2):
        if (message_text == "Вперёд"):
            await message.reply_photo(
                "https://ibb.co/x1pJ9xq",
                "",
                reply_markup=keyboard_full)
            count_prez[username] += 1
        elif (message_text == "Назад"):
            await message.reply_photo(
                "https://ibb.co/JqjWQnN",
                "",
                reply_markup=keyboard_start)
            count_prez[username] -= 1
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 3):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/JxDQ3fs",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/bHn466s",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 4):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/tHCGQkf",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/x1pJ9xq",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 5):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/wrkz9Hb",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/JxDQ3fs",
                "",
                reply_markup=keyboard_full)

        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 6):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/cQ1wY4V",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/tHCGQkf",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 7):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/WxLb87F",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/wrkz9Hb",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 8):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/bBP0KF6",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/cQ1wY4V",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 9):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/64gLQNP",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/WxLb87F",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 10):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/wcw5M0X",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/bBP0KF6",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 11):
        if (message_text == "Вперёд"):
            count_prez[username] += 1
            await message.reply_photo(
                "https://ibb.co/LnJk684",
                "",
                reply_markup=keyboard_end)
        elif (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/64gLQNP",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")
    elif (count_prez[username] == 12):
        if (message_text == "Назад"):
            count_prez[username] -= 1
            await message.reply_photo(
                "https://ibb.co/wcw5M0X",
                "",
                reply_markup=keyboard_full)
        elif (message_text == "Выйти из презентации"):
            await message.reply_text("Вы вышли из презентации", reply_markup=keyboard_0)
        else:
            await message.reply_text("Такого варианта не существует😯")





    '''if(message == 'В 30' and countable == 1):
        await message.reply_text("Верно")
        count += 1
        countable += 1
    else:
        await message.reply_text("Неверно")
        countable += 1
    but3_1 = KeyboardButton('19.000')
    but3_2 = KeyboardButton('Примерно 38.000')
    but3_3 = KeyboardButton('Порядка 30.000')
    keyboard4 = ReplyKeyboardMarkup([[but3_1], [but3_2], [but3_3]])
    await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpeGrn047P2tXQo4lvL8x0WC0TKph2-mWhxK9gziE&s","3.	Сколько нефтедобывающих скважин в арсенале Лукойла?", reply_markup=keyboard4)
    if(message == 'Порядка 30.000' and countable == 2):
        await message.reply_text("Верно")
        count += 1
        countable += 1
    else:
        await message.reply_text("Неверно")
        countable += 1
    but4_1 = KeyboardButton('Лазаревское, Углич, Киржач')
    but4_2 = KeyboardButton('Лангепас, Урай, Когалым')
    but4_3 = KeyboardButton('Лабинск, Улейма, Кашпир')
    keyboard5 = ReplyKeyboardMarkup([[but4_1], [but4_2], [but4_3]])
    await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpeGrn047P2tXQo4lvL8x0WC0TKph2-mWhxK9gziE&s", "4.	От первых букв названия каких городов происходит ЛУК в названии Лукойл? ", reply_markup=keyboard5)
    if (message == 'Лангепас, Урай, Когалым' and countable == 3):
        await message.reply_text("Верно")
        count += 1
        countable += 1
    else:
        await message.reply_text("Неверно")
        countable += 1'''
    #await message.reply_text(message)
    #await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpeGrn047P2tXQo4lvL8x0WC0TKph2-mWhxK9gziE&s", "Дароу старый!")
    #await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFLYH79n5BowDE27E0gnHoJA1PA29dqCeBlDQYaFo&s","Не понимать(")


def main() -> None:
    application = Application.builder().token("<PASTE_YOUR_TELEGRAM_TOKEN_HERE>").build()
    application.add_handler(MessageHandler(filters.TEXT | filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(echo))
    application.run_polling()


if __name__ == "__main__":
    main()