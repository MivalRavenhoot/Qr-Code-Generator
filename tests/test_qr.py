import os, pytest, qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from src.telegram_py_bot import QR

def test_qr():
    test_url = "https://google.it"
    QR(test_url)

    # test qrcode png image generation
    assert os.path.exists('qrcode.png') == True

    # test correct qrcode generation
    decocdeQR = decode(Image.open('qrcode.png'))
    assert decocdeQR[0].data.decode('ascii') == test_url
