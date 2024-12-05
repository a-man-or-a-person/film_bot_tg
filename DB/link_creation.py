import os

from dotenv import load_dotenv


def connection_link():
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT")
    host = os.getenv("DB_HOST")
    db_pass = os.getenv("DB_PASS")
    db_user = os.getenv("DB_USER")
    return f"postgresql+asyncpg://{db_user}:{db_pass}@{host}:{port}/{db_name}"


# print(connection_link())
