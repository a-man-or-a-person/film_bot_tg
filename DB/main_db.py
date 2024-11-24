import asyncio

from DB.orm import create_tables, insert_workers, admin_insert_film


async def main():
    pass
    # await create_tables()
    # await insert_workers()
    # await admin_insert_film(**{'name': 'Django', 'source_film': 'https://git'})

if __name__ == '__main__':
    asyncio.run(main())