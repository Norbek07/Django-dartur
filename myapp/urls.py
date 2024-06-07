from django.urls import path
from .views import hello_word

urlpatterns = [
    path('',hello_word,name="hello_word")
]