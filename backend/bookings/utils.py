import qrcode
from django.core.files.base import ContentFile
from io import BytesIO

def generate_qr(data):
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer)
    return ContentFile(buffer.getvalue())
