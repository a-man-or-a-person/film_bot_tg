from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest

from bot.wrappers import AdminAuthorization


@pytest.mark.asyncio
async def test_non_admin_cannot_reach_handler():
    event = SimpleNamespace(from_user=SimpleNamespace(id=42), answer=AsyncMock())
    handler = AsyncMock()
    with patch("bot.wrappers.get_admins", AsyncMock(return_value=set())):
        await AdminAuthorization()(handler, event, {})
    handler.assert_not_awaited()
    event.answer.assert_awaited_once()


@pytest.mark.asyncio
async def test_permissions_are_checked_again_on_each_step():
    event = SimpleNamespace(from_user=SimpleNamespace(id=42), answer=AsyncMock())
    handler = AsyncMock()
    middleware = AdminAuthorization()
    with patch("bot.wrappers.get_admins", AsyncMock(side_effect=[{42}, set()])):
        await middleware(handler, event, {})
        await middleware(handler, event, {})
    assert handler.await_count == 1


@pytest.mark.asyncio
async def test_admin_callbacks_are_protected_in_dispatcher():
    from aiogram import Bot, Dispatcher
    from aiogram.types import Update
    from bot.handlers.admin_handler import admin_router
    from bot.handlers.film_actions_handler import film_router

    dispatcher = Dispatcher()
    dispatcher.include_router(admin_router)
    dispatcher.include_router(film_router)
    bot = Bot("123456:TEST_ONLY_TOKEN")
    try:
        for action in ("add_admin", "delete_film_admin"):
            update = Update.model_validate({"update_id": 1, "callback_query": {
                "id": "test", "from": {"id": 42, "is_bot": False, "first_name": "Test"},
                "chat_instance": "test", "data": action,
                "message": {"message_id": 1, "date": 0, "chat": {"id": 42, "type": "private"}}
            }})
            with patch("bot.wrappers.get_admins", AsyncMock(return_value=set())), patch.object(bot.session, "make_request", AsyncMock(return_value=True)):
                await dispatcher.feed_update(bot, update)
            state = dispatcher.fsm.get_context(bot=bot, chat_id=42, user_id=42)
            assert await state.get_state() is None
    finally:
        await dispatcher.storage.close()
        await bot.session.close()
