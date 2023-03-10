#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import asyncio
import logging  # логирование бота
from aiogram import Bot, Dispatcher, executor, types  # библиотека для телеграм бота
import scr
import weather
import sqlite
import aioschedule as schedule  # работа по расписанию

# объект бота
bot = Bot(token=scr.token_bot)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)  # Логирование


@dp.message_handler(content_types=['text'])
async def send_message(message: types.Message):
    message_lower = message.text

    if message_lower.lower() == "погода":
        data_w = weather.request_current_weather(1)
        string_message = weather.make_message_weather(data_w)

        await message.answer(string_message)  # отправка сообщения пользователю

    # elif message_lower.lower() == "погода дома":
    #    string_message = weather.make_message_weather_home()

    #    bot.send_message(message.from_user.id, string_message)  # отправка сообщения пользователю

    elif message_lower.lower() == "подписка на погоду" or "отписаться":
        string_message = sqlite.subscribe(message.from_user.id, message.text)

        try:
            await message.answer(string_message)

        except Exception as e:  # Выкидываем исключение если фраза не запрограмированна
            await message.answer('Я тебя не понял')
            print("Exception (forecast):", e)
            pass


async def time_message():  # Формирование сообщения по времени
    global count_2
    count_2 = 0
    all_user = sqlite.read_id()

    data_w = weather.request_current_weather(1)
    string_message_weather = weather.make_message_weather(data_w)
    # string_message_home = weather.make_message_weather_home()
    string_message = string_message_weather  # + '\n \n' + string_message_home

    count = len(all_user)

    while count != count_2:
        await bot.send_message(all_user[count_2][0], string_message)
        count_2 += 1


async def job():  # запуск по расписанию
    schedule.every().monday.at('09:00').do(time_message)
    schedule.every().tuesday.at('09:00').do(time_message)
    schedule.every().wednesday.at('09:00').do(time_message)
    schedule.every().thursday.at('09:00').do(time_message)
    schedule.every().friday.at('09:00').do(time_message)
    schedule.every().saturday.at('12:00').do(time_message)
    schedule.every().sunday.at('12:00').do(time_message)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(job())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # совместить работу aiogram и schedule на Тelegram bot
