import sqlite3
from random import shuffle
from Person import Student
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

token = '6101753173:AAFACNkib17bXwxN_P6IDAuHMIWv-ReRMik'

bot = Bot(token)
dp = Dispatcher(bot)
user = Student()
all_math = []
all_ict = []
all_biology = []


@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    global all_math, all_ict, all_biology
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    math = types.InlineKeyboardButton(text='Математика', callback_data='math')
    ict = types.InlineKeyboardButton(text='ICT', callback_data='ict')
    biology = types.InlineKeyboardButton(text='Биология', callback_data='biology')
    keyboard.add(math, ict)
    keyboard.add(biology)
    user.start_keyboard = keyboard
    await bot.send_message(message.chat.id, f'Салом {message.chat.first_name} ! Ин бот барои санҷиши тестӢ мебошад')
    await bot.send_message(message.chat.id, 'Фанни худро интихоб кунед', reply_markup=keyboard)
    sqlite_con = sqlite3.connect('data.db')
    cursor = sqlite_con.cursor()
    cursor.execute('SELECT * FROM math')
    all_math = cursor.fetchall()
    cursor.execute('SELECT * FROM ict')
    all_ict = cursor.fetchall()
    cursor.execute('SELECT * FROM biology')
    all_biology = cursor.fetchall()
    cursor.close()
    sqlite_con.close()


@dp.callback_query_handler(lambda button: button.data == 'math')
async def math(callback):
    await bot.send_message(callback.from_user.id, 'Шумо фанни Математикаро интихоб кардед')
    user.p_otvet = 0
    user.subject = 'math'

    await math_test(callback.from_user.id)


@dp.callback_query_handler(lambda button: button.data == 'ict')
async def ict(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Шумо фанни Информатикаро интихоб кардед')
    user.p_otvet = 0
    user.subject = 'ict'
    await ict_test(callback.from_user.id)


@dp.callback_query_handler(lambda button: button.data == 'biology')
async def biology(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Шумо фанни Биологияро интихоб кардед')
    user.p_otvet = 0
    user.subject = 'biology'
    await biology_test(callback.from_user.id)


async def math_test(id: int):
    # await bot.send_message(id, 'саволҳо')
    try:
        savol = all_math[0][0]
        v1, v2, v3 = all_math[0][1], all_math[0][2], all_math[0][3]
        user.correct = v1
        vars = [v1, v2, v3]
        shuffle(vars)
        user.vars = vars
        v1, v2, v3 = vars
        user.edited_message = savol + '\n' + v1 + '\n' + v2 + '\n' + v3
        variants = types.InlineKeyboardMarkup(row_width=1)
        v1 = types.InlineKeyboardButton(text=v1, callback_data=v1)
        v2 = types.InlineKeyboardButton(text=v2, callback_data=v2)
        v3 = types.InlineKeyboardButton(text=v3, callback_data=v3)
        variants.add(v1)
        variants.add(v2)
        variants.add(v3)
        await bot.send_message(id, savol, reply_markup=variants)
        all_math.remove(all_math[0])
    except IndexError:
        await bot.send_message(id, f'Санҷиши тестӣ ба охир расид.\nШумораи ҷавобҳои дуруст {user.p_otvet}')
        await yesorno(id)


async def ict_test(id: int):
    # await bot.send_message(id, 'саволҳо')
    try:
        savol = all_ict[0][0]
        v1, v2, v3 = all_ict[0][1], all_ict[0][2], all_ict[0][3]
        user.correct = v1
        vars = [v1, v2, v3]
        shuffle(vars)
        user.vars = vars
        v1, v2, v3 = vars
        user.edited_message = savol + '\n' + v1 + '\n' + v2 + '\n' + v3
        variants = types.InlineKeyboardMarkup(row_width=1)
        v1 = types.InlineKeyboardButton(text=v1, callback_data=v1)
        v2 = types.InlineKeyboardButton(text=v2, callback_data=v2)
        v3 = types.InlineKeyboardButton(text=v3, callback_data=v3)
        variants.add(v1)
        variants.add(v2)
        variants.add(v3)
        await bot.send_message(id, savol, reply_markup=variants)
        all_ict.remove(all_ict[0])
    except IndexError:
        await bot.send_message(id, f'Санҷиши тестӣ ба охир расид.\nШумораи ҷавобҳои дуруст {user.p_otvet}')
        await yesorno(id)


async def biology_test(id: int):
    # await bot.send_message(id, 'саволҳо')
    try:
        savol = all_biology[0][0]
        v1, v2, v3 = all_biology[0][1], all_biology[0][2], all_biology[0][3]
        user.correct = v1
        vars = [v1, v2, v3]
        shuffle(vars)
        user.vars = vars
        v1, v2, v3 = vars
        user.edited_message = savol + '\n' + v1 + '\n' + v2 + '\n' + v3
        variants = types.InlineKeyboardMarkup(row_width=1)
        v1 = types.InlineKeyboardButton(text=v1, callback_data=v1)
        v2 = types.InlineKeyboardButton(text=v2, callback_data=v2)
        v3 = types.InlineKeyboardButton(text=v3, callback_data=v3)
        variants.add(v1)
        variants.add(v2)
        variants.add(v3)
        await bot.send_message(id, savol, reply_markup=variants)
        all_biology.remove(all_biology[0])
    except IndexError:
        await bot.send_message(id, f'Санҷиши тестӣ ба охир расид.\nШумораи ҷавобҳои дуруст {user.p_otvet}')
        await yesorno(id)


async def yesorno(user_id: int):
    again_buttons = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton(text='Бале', callback_data='yes')
    b2 = types.InlineKeyboardButton(text='Не', callback_data='no')
    again_buttons.add(b1, b2)
    await bot.send_message(user_id, 'Мехоҳед санҷиши тестиро аз нав оғоз кунед?', reply_markup=again_buttons)


@dp.callback_query_handler(lambda callback: callback.data in user.vars)
async def check(callback: types.CallbackQuery):
    user.edited_message = user.edited_message.replace(user.correct, f'<b><i>{user.correct}</i></b>✅')

    if callback.data == user.correct:
        user.p_otvet += 1
    else:
        user.edited_message = user.edited_message.replace(callback.data, callback.data + '❓')

    await callback.message.edit_text(user.edited_message, parse_mode='HTML')
    if user.subject == 'math':
        await math_test(callback.from_user.id)
    elif user.subject == 'ict':
        await ict_test(callback.from_user.id)
    elif user.subject == 'biology':
        await biology_test(callback.from_user.id)


@dp.callback_query_handler(lambda callback: callback.data == 'yes')
async def yes(callback: types.CallbackQuery):
    global all_math, all_ict, all_biology
    await bot.send_message(callback.from_user.id, 'Фанро интихоб кунед', reply_markup=user.start_keyboard)

    sqlite_con = sqlite3.connect('data.db')
    cursor = sqlite_con.cursor()
    cursor.execute('SELECT * FROM math')
    all_math = cursor.fetchall()
    cursor.execute('SELECT * FROM ict')
    all_ict = cursor.fetchall()
    cursor.execute('SELECT * FROM biology')
    all_biology = cursor.fetchall()
    cursor.close()
    sqlite_con.close()


@dp.callback_query_handler(lambda callback: callback.data == 'no')
async def no(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id,
                           'Санҷиши тестӣ ба охир расид.\nБарои аз нав оғоз кардани санҷиш командаи /start -ро пахш кунед')


executor.start_polling(dp, skip_updates=True)
