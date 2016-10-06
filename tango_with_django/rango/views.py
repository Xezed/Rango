from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'boldmessage' : 'This is the bold message HELLO WORLD!'}

    return render(request, 'rango/index.html', context)


def about(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/">Go to the main page</a>')