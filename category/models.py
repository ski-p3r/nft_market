import os
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class ImageExtensionValidator:
    def __call__(self, value):
        allowed_extensions = ['.png']
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in allowed_extensions:
            raise ValidationError('Unsupported file extension.')

validate_image_extension = ImageExtensionValidator()

class Category(models.Model):
    category_name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=50, unique=True)
    category_image  = models.ImageField(upload_to='CategoryIcon', blank=True, validators=[validate_image_extension])
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    