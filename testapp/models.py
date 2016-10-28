from django.db import models
from tinymce.models import HTMLField
from gallery.models import GalleryImageField


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = GalleryImageField()
    content = HTMLField()
