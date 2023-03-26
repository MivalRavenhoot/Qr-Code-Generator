from src.telegram_py_bot import start
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_start():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()
    context.bot.send_message.return_value = "some value"

    await start(update, context)

    context.bot.send_message.assert_called_with(
        chat_id=update.effective_chat.id,
        text="Welcome to the QR generator bot!\nSend /help to see the usage",
    )
