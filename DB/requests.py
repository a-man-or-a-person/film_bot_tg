from DB.database import async_session_factory
from DB.models import UserOrm, FilmOrm, FavoriteOrm
from sqlalchemy import select, update, delete


async def set_user(tg_id: int) -> None:
    async with async_session_factory() as session:
        user = await session.scalar(select(UserOrm).where(UserOrm.tg_id == tg_id))

        if not user:
            new_user = UserOrm(tg_id=tg_id, user_name='')
            session.add(new_user)
            await session.commit()
