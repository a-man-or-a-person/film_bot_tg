import asyncio

from DB.orm import admin_insert_film, create_tables, insert_workers


async def main():
    pass
    await create_tables()
    # await admin_insert_film(**{'name': 'Django', 'source_film': 'https://git'})


if __name__ == "__main__":
    asyncio.run(main())
