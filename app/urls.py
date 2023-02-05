
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('trad/', views.trad, name='trad'),
    path('corrector/', views.corrector, name='corrector'),
]
