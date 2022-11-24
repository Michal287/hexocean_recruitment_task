from io import BytesIO
from PIL import Image as PilImage
from django.core.files.base import ContentFile


def create_exist_image(image, convert, ext='png', quality=95):
    ext = 'jpeg' if ext.lower() == 'jpg' else ext
    filename = str(image).split('/')[-1].split('.')

    with PilImage.open(image) as image:
        buff_image = BytesIO()
        binary_image = image.convert(convert)
        binary_image.save(buff_image, ext, quality=quality)

        return ContentFile(buff_image.getvalue(), f'{filename}-binary.{ext}')