from django.urls import path
from .views import index, contacto

urlpatterns = [
              path('', index, name='index'),
              path('contact.html', contacto, name='contacto'),
              
]