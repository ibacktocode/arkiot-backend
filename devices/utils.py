import pyqrcode

QR_CODES_FOLER = 'static/devices/qr_codes/'

def save_qr_code(data):
    img = pyqrcode.create(data)
    img.png(QR_CODES_FOLER + data + '.png')