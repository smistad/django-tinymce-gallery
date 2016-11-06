from django.db import models
from gallery.models import GalleryImageField, RichTextFormatField


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = GalleryImageField()
    content = RichTextFormatField()
