# Film discovery Telegram bot

A Python learning project using aiogram, SQLAlchemy's asynchronous sessions and the Kinopoisk API.

## Implemented scope

- Telegram menus for film lookup, ranked selections and random selections.
- Film catalog operations and administrator management.
- Pydantic models for API responses and submitted film data.

The current selection logic is not a trained ML recommender.

## Setup

Create and activate a Python virtual environment, then run:

```sh
python -m pip install -r requirements.txt
```

Create a local `.env` (never commit real credentials):

```dotenv
BOT_TOKEN=
KINOPOISK_API_KEY=
SELECTED_DB=SQLITE
```

For PostgreSQL set `SELECTED_DB=POSTGRES` and provide `DB_NAME`, `DB_PORT`, `DB_HOST`, `DB_PASS` and `DB_USER`.
Use an isolated demo database and a test bot.

```sh
python main.py
```

The entry point is `main.py`; the Telegram library is aiogram.

## Layout

- `bot/handlers/`: user menus, administrative callbacks and film editing states.
- `apis/kinopoisk.py`: external film API calls.
- `Pydantic/`: validation models.
- `DB/`: models, sessions and database requests.

## Current limitations

- Administrative callbacks and state handlers do not consistently verify permissions. Do not deploy to untrusted users before fixing authorization throughout these flows.
- `DB/orm.py:create_tables` drops existing tables before recreating them. Do not use it to initialize a database containing data.
- SQLite uses a Windows-style path in `DB/database.py`; portability requires a follow-up fix.
- The repository includes a SQLite database. Its records have not been certified as safe sample data.
- API requests use synchronous HTTP calls inside asynchronous functions.
- There is no automated test suite or CI workflow in the default-branch tree reviewed for this documentation.

Previously exposed API credentials require rotation even after removing them from source.

## License

See [LICENSE](LICENSE). No license terms were changed.
