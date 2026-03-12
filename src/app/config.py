import os
from dotenv import load_dotenv

load_dotenv()

# ...//postgres:password@db:5432/usersdb
_DATABASE_URL = os.getenv("DATABASE_URL")

def get_database_url(url: str) -> str:

    'Tolgo l\'host \'db\' e metto \'localhost\' se lo script è eseguito fuori da docker'
    if url and "@db" in url:
        if not os.path.exists('/.dockerenv'):
            return url.replace("@db", "@localhost")
    return url


DATABASE_URL = get_database_url(_DATABASE_URL)
SECRET_KEY = os.getenv("SECRET_KEY")