from utils.db_api.database import create_db


# from loader import bot
 #import middlewares, filters, handlers

from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
import filters
import middlewares

filters.setup(dp)
middlewares.setup(dp)
from utils.notify_admins import on_startup_notify

await on_startup_notify(dp)
await create_db()

if __name__ == '__main__':
    from aiogram import executor

    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
