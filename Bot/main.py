import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "8465536900:AAEw0TY2pf-TaB3_FI8s2bADLubCIBU2kxU"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🎟 Розыгрыши", callback_data="menu_draws"),
        InlineKeyboardButton("➕ Создать розыгрыш", callback_data="menu_create"),
        InlineKeyboardButton("📜 История", callback_data="menu_history"),
    )
    return kb


@dp.message_handler(commands=["start", "menu"])
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать! Выберите раздел:",
        reply_markup=main_menu()
    )


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("menu_"))
async def process_menu(call: types.CallbackQuery):
    await call.answer() 
    key = call.data.removeprefix("menu_")

    if key == "draws":
        await call.message.edit_text(
            "📋 Розыгрыши:\n(здесь будет два таба — ‘Участвую’ и ‘Все розыгрыши’)",
            reply_markup=None
        )
    elif key == "create":
        await call.message.edit_text(
            "🛠 Создание розыгрыша:\n(заготовки шагов)",
            reply_markup=None
        )
    elif key == "history":
        await call.message.edit_text(
            "📖 История:\n(Ваши конкурсы и участия)",
            reply_markup=None
        )


async def on_startup(_):
    print("Бот запущен")


if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)