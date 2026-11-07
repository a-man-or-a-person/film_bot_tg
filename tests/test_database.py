from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
import pytest

import DB.orm as orm


@pytest.mark.asyncio
async def test_initialization_preserves_existing_data(tmp_path, monkeypatch):
    engine = create_async_engine('sqlite+aiosqlite:///' + (tmp_path / 'demo.db').as_posix())
    monkeypatch.setattr(orm, 'async_engine', engine)
    try:
        await orm.create_tables()
        async with engine.begin() as conn:
            await conn.execute(text("INSERT INTO users (id, tg_id, user_name) VALUES (1, 42, 'demo')"))
        await orm.create_tables()
        async with engine.connect() as conn:
            assert await conn.scalar(text('SELECT count(*) FROM users')) == 1
    finally:
        await engine.dispose()
