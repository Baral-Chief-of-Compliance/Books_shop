from django.shortcuts import render


def index(request):
    return render(request, 'Books_Shop_Site/index.html')
