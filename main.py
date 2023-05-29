import logging

from aiogram import Bot, Dispatcher, executor, types
from test import audio_yukla_ber
API_TOKEN = '6032377757:AAHpKeg1mBiIRLsBqIKKEK8MmbknlJDznxE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu insta bot")



@dp.message_handler()
async def echo(message: types.Message):
    mes_text = message.text
    audio_link = audio_yukla_ber(mes_text)
    await message.answer("Audio yuklanmoqda")
    await message.answer_audio(audio_link,caption="Bu zo'r audio. Murojaat uchun @Asadbek")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    