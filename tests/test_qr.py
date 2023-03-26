import os, pytest
from pyzbar.pyzbar import decode
from PIL import Image
from src.telegram_py_bot import qr_generator, QR
from unittest.mock import AsyncMock

def test_qr():
    test_url = "https://google.it"
    QR(test_url)

    # test qrcode png image generation
    assert os.path.isfile('qrcode.png')

    # test correct qrcode generation
    decocdeQR = decode(Image.open('qrcode.png'))
    assert decocdeQR[0].data.decode('ascii') == test_url

@pytest.mark.asyncio
async def test_qr_generator():
    update = AsyncMock()
    context = AsyncMock()
    await qr_generator(update, context)

    assert os.path.isfile('qrcode.png')
