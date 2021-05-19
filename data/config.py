import os
from dotenv import load_dotenv

load_dotenv()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Заберем данные для подключения к базе данных (юзер, пароль, название бд) - тоже прописать в файле ".env"
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

# Ссылка подключения к базе данных
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
#from environs import Env
# Теперь используем вместо библиотеки python-dotenv библиотеку environs
#env = Env()
#env.read_env()

#BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
#ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
#IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
