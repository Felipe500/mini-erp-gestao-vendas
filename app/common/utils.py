from pathlib import Path
from PIL import Image
from io import BytesIO

import uuid
import posixpath
from datetime import datetime

from django.core.files import File
from django.core.files.utils import validate_file_name
from django.db import models

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def image_resize(image, width, height):
    with Image.open(image) as img:
        if img.width > width or img.height > height:
            output_size = (width, height)
            img.thumbnail(output_size, Image.LANCZOS)
            img_filename = Path(image.file.name).name
            img_suffix = Path(image.file.name).name.split(".")[-1]
            img_format = image_types[img_suffix]
            buffer = BytesIO()
            img.save(buffer, format=img_format)
            file_object = File(buffer)
            image.save(img_filename, file_object)


def _generate_filename(inst_upload_to, filename) -> str:
    ext = filename.split('.')[-1]
    hash_name = str(uuid.uuid4())
    filename = f"{hash_name}.{ext}"
    upload_to = f"{inst_upload_to}/%Y/%m/%d/"
    dirname = datetime.now().strftime(upload_to)
    filename = posixpath.join(dirname, filename)
    filename = validate_file_name(filename, allow_relative_path=True)
    return filename


class FileField(models.FileField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


class ImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


def format_price_(val):
    return f'Total: R$ {val:.2f}'.replace('.', ',')
