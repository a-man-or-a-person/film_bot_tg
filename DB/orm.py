from DB.database import Base, async_engine, async_session_factory
from DB.models import FilmOrm, UserOrm


async def create_tables():
    async with async_engine.connect() as conn:
        async_engine.echo = True
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()


async def insert_workers():
    async with async_session_factory() as session:
        worker_jack = UserOrm(user_name="Jack")
        worker_michael = UserOrm(user_name="Michael")
        session.add_all([worker_jack, worker_michael])
        await session.commit()


async def admin_insert_film(**kwargs):
    async with async_session_factory() as session:
        new_film = FilmOrm(**kwargs)
        session.add(new_film)
        await session.commit()
