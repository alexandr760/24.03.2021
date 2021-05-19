from utils.db_api.db_commands import add_item

import asyncio

from utils.db_api.database import create_db

# Используем эту функцию, чтобы заполнить базу данных
async def add_items():
    await add_item(name="",
                   category_name="Информация", category_code="Information",
                   subcategory_name="книги", subcategory_code="book",
                    photo="-")
    await add_item(name="Скрипты",
                   category_name="программы", category_code="Information",
                   subcategory_name="текст", subcategory_code="ошибки",
                   photo="-")
    await add_item(name="Эксплойты",
                   category_name="Информация", category_code="Information",
                   subcategory_name="Уязвимости", subcategory_code="info",
                    photo="-")

loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_items())