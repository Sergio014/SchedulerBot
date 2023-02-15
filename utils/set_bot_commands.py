from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести справку"),
            types.BotCommand("newcase", "Додати нове завдання/справу"),
            types.BotCommand("mycases", "Всі заплановані справи"),
            types.BotCommand("exit", "Скасовує поточну дію"),
        ]
    )
