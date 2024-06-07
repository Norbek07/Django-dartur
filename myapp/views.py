from django.shortcuts import render
from django.http import HttpResponse





def hello_word(request):
    return render(request=request,template_name="index.html")
