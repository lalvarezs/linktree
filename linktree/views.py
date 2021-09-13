from django.shortcuts import render
from django.http import HttpResponse
from linktree.models import Link
# Create your views here.
def home_page_view(request):
    links = Link.objects.filter(owner=Link.Owner.IMOBILIARIA)
    return render(request, 'linktree/home_page.html',{'links': links})

def construtora_page_view(request):
    construtora_links = Link.objects.filter(owner=Link.Owner.CONSTRUTORA)
    return render(request, 'linktree/construtora_page.html',{'construtora_links': construtora_links})