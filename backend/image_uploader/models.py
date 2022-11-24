from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.storage import default_storage
from django.utils import timezone
from datetime import timedelta
import hashlib


class TierThumbnail(models.Model):
    size = models.SmallIntegerField(validators=[MinValueValidator(16), MaxValueValidator(4320)])

    def __str__(self):
        return f"size: {self.size}x{self.size}"


class Tier(models.Model):
    name = models.CharField(max_length=32)
    image_link = models.BooleanField(default=False)
    download_binary_image_link = models.BooleanField(default=False)
    tier_thumbnail_size = models.ManyToManyField(TierThumbnail, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, default=None, null=True)


def image_path(instance, filename):
    return f'image/users/{instance.user.id}/{filename}'


def binary_image_path(instance, filename):
    return f'image/users/{instance.user.id}/binary/{filename}'


class BinaryImage(models.Model):
    binary_image = models.ImageField(upload_to=binary_image_path, blank=False)
    binary_image_link = models.CharField(blank=False, max_length=32, unique=True)
    created = models.DateTimeField(default=timezone.now)
    expiration_time = models.SmallIntegerField(validators=[MinValueValidator(300), MaxValueValidator(30000)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        if self.binary_image is not None:
            path = self.binary_image.name
            if path:
                default_storage.delete(path)

        super(BinaryImage, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        seed = (str(self.created) + self.binary_image.name)
        self.binary_image_link = hashlib.md5(seed.encode('utf-8')).hexdigest()[:16]

        super(BinaryImage, self).save(*args, **kwargs)

    def is_expired(self):
        return (self.created + timedelta(seconds=self.expiration_time)) < timezone.now()

    def __str__(self):
        return f"Image binary: {self.pk}"


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_path, blank=False)
    binary_image = models.OneToOneField(BinaryImage, on_delete=models.CASCADE,
                                        default=None, null=True, blank=True, related_name='image')

    def get_extension(self):
        return self.image.name.split(".")[1]

    def __str__(self):
        return f"Image {self.pk}"
