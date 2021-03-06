from django.db import models
from .widgets import SelectImage, RichTextFormatWidget
from django.contrib.admin import widgets as admin_widgets


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.file.url + ':' + self.name


class GalleryImageField(models.ForeignKey):
    # Set foreign key to Image
    def __init__(self, on_delete=None, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, **kwargs):
        kwargs['to'] = 'gallery.image'
        super(GalleryImageField, self).__init__(on_delete=on_delete, related_name=related_name,
                related_query_name=related_query_name, limit_choices_to=limit_choices_to,
                parent_link=parent_link, to_field=to_field, db_constraint=db_constraint, **kwargs)

    # Override widget
    def formfield(self, **kwargs):
        defaults = {'widget': SelectImage}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        # Needed?
        #if defaults['widget'] == admin_widgets.AdminTextareaWidget:
        #    defaults['widget'] = tinymce_widgets.AdminTinyMCE

        return super(GalleryImageField, self).formfield(**defaults)


class RichTextFormatField(models.TextField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms.
    """
    def formfield(self, **kwargs):
        defaults = {'widget': RichTextFormatWidget}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = RichTextFormatWidget

        return super(RichTextFormatField, self).formfield(**defaults)
