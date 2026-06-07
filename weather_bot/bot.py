import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart, Command
from weather import get_current_weather, get_forecast

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я бот погоды.\n\n"
        "Команды:\n"
        "🌤 /weather <город> — текущая погода\n"
        "📅 /forecast <город> — прогноз на 3 дня\n\n"
        "Пример: /weather Москва"
    )


@dp.message(Command("weather"))
async def cmd_weather(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажи город: /weather Москва")
        return

    city = args[1].strip()
    await message.answer(f"🔍 Ищу погоду для «{city}»...")

    result = await asyncio.to_thread(get_current_weather, city)
    await message.answer(result, parse_mode="HTML")


@dp.message(Command("forecast"))
async def cmd_forecast(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Укажи город: /forecast Москва")
        return

    city = args[1].strip()
    await message.answer(f"🔍 Ищу прогноз для «{city}»...")

    result = await asyncio.to_thread(get_forecast, city)
    await message.answer(result, parse_mode="HTML")


@dp.message(F.text & ~F.text.startswith("/"))
async def handle_plain_text(message: Message):
    """Если написали просто название города без команды"""
    city = message.text.strip()
    await message.answer(f"🔍 Ищу погоду для «{city}»...\n<i>Подсказка: используй /forecast {city} для прогноза</i>", parse_mode="HTML")
    result = await asyncio.to_thread(get_current_weather, city)
    await message.answer(result, parse_mode="HTML")


async def main():
    await bot.set_my_commands([
        BotCommand(command="weather", description="Текущая погода"),
        BotCommand(command="forecast", description="Прогноз на 3 дня"),
    ])
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
