from src.telegram_py_bot import printing
from unittest.mock import AsyncMock, Mock
import pytest

@pytest.mark.asyncio
async def test_printing():
    update = Mock()
    context = Mock()
    text = 'Test'
    context.bot.send_message = AsyncMock()

    await printing(update, context, text)

    context.bot.send_message.assert_called_once_with(
        chat_id=update.effective_chat.id,
        text=f'You requested the following string: "{text}"\n\nThis is the generated QR code image:')
