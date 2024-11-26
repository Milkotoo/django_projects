# hello_app/urls.py
# hello_app/urls.py
from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),  # Ви можете використовувати порожній шлях, щоб обробляти hello/
]
