from django.urls import path
from .views import hello_word

urlpatterns = [
    path('',hello_world,name="hello-world")
]