from django.shortcuts import render
from .models import Article


def index(request):
    return render(request, 'testapp/index.html', {'articles': Article.objects.all()})

