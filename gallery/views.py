from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from gallery.forms import ImageUploadForm
from gallery.models import Image


@staff_member_required
def browser(request):
    template = 'gallery/filebrowser.html'
    upload_form = ImageUploadForm()
    uploaded_file = None
    upload_tab_active = False

    files = Image.objects.all()

    if request.POST:
        upload_form = ImageUploadForm(request.POST, request.FILES)
        upload_tab_active = True

        if upload_form.is_valid():
            uploaded_file = upload_form.save(commit=False)
            uploaded_file.save()

    data = {
        'files': files,
        'upload_form': upload_form,
        'uploaded_file': uploaded_file,
        'upload_tab_active': upload_tab_active,
        'is_images_dialog': True,
        'is_documents_dialog': False,
    }

    return render(request, template, data)
