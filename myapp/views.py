from django.shortcuts import render
from django.http import HttpResponse





def hello_word(request):
    return HttpResponse("<h1>Assalomu aleykum Norbek</h1>")
