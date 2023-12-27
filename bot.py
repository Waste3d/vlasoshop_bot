from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot('')
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add("Корзина").add("Контакты").add("Админ-панель")

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add("Создать рассылку")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMqZYvsdtOGJHU4dGESjpzgMdfXXL4AAiEbAAIMzVlJiEJP7zBb_XgzBA')
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать в наш магазин!',
                         reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)
    

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer('Каталог пуст!')

@dp.message_handler(text='Корзина')
async def bin(message: types.Message):
    await message.answer('Корзина пуста!')

@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Owners - @waste3d, @r0reee \n ТП, по вопросам рекламы - @oekjjj')

@dp.message_handler(text='Админ-панель')
async def admin_paanel(message: types.Message):
    await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)
    else:
        await message.answer(f'Обманывать плохо!')


    

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю. Попробуй еще раз.')


if __name__ == '__main__':
    executor.start_polling(dp)
