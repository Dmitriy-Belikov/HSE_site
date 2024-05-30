from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.core.paginator import Paginator

from django.views.generic import DetailView


def index(request):
    forms = News.objects.all()[::-1]
    paginator = Paginator(forms, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'main/index.html', {'page_obj': page_obj})

def about(request):
    return render(request, 'main/about.html')



