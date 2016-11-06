from django import forms
from django.forms import widgets
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
import tinymce.widgets


class SelectImage(widgets.Widget):

    def __init__(self, attrs=None, choices=()):
        super(SelectImage, self).__init__(attrs)
        # choices can be any iterable, but we may need to render this widget
        # multiple times. Thus, collapse it into a list so it can be consumed
        # more than once.
        self.choices = list(choices)

    def render(self, name, value, attrs=None):
        string = '<select class="image_select" name="' + name + '">'
        for id, image in self.choices:
            if value == id:
                string += '<option value="' + str(id) + '" selected>' + image + '</option>'
            else:
                string += '<option value="' + str(id) + '">' + image + '</option>'
        string += '</select>'

        return mark_safe(string)

    class Media:
        js = (
              'gallery/js/select_image.js',
              'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js',
              )
        css = {'all': ('https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css',)}


class RichTextFormatWidget(tinymce.widgets.TinyMCE):
    # Override media
    def _media(self):
        if tinymce.settings.USE_COMPRESSOR:
            js = [reverse('tinymce-compressor')]
        else:
            js = [tinymce.settings.JS_URL]
        # TODO add gallery brower init script here
        js.append('django_tinymce/init_tinymce.js')
        js.append('gallery/js/gallery_browser_init.js')
        return forms.Media(js=js)
    media = property(_media)

