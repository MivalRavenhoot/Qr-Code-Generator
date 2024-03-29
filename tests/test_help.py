from src.telegram_py_bot import help
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_help():
    update = Mock()
    context = Mock()
    context.bot.send_message = AsyncMock()

    await help(update, context)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text="Usage:\nwrite the string you want to convert into a QR code image",
    )
