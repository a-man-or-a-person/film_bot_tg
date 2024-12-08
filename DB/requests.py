from sqlalchemy import delete, insert, select, update

from DB.database import async_session_factory
from DB.models import FavoriteOrm, FilmOrm, UserOrm


async def set_user(tg_id: int) -> None:
    async with async_session_factory() as session:
        user = await session.scalar(select(UserOrm).where(UserOrm.tg_id == tg_id))
        if not user:
            new_user = UserOrm(tg_id=tg_id, user_name="")
            session.add(new_user)
            await session.commit()


async def delete_film(film_id: int) -> None:
    async with async_session_factory() as session:
        stmt = select(FilmOrm).where(FilmOrm.film_id == film_id)
        result = await session.execute(stmt)
        selected_film = result.scalar_one_or_none()

        if selected_film:
            await session.delete(selected_film)
            await session.commit()


async def add_film(**kwargs) -> None:
    '''
    Some explanations
    '''
    async with async_session_factory() as session:
        new_film = FilmOrm(**kwargs)
        session.add(new_film)
        await session.commit()
