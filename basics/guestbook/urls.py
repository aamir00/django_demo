from django.urls import path
from . import views

#Providing url names that can be used further

urlpatterns = [
    path('', views.index, name='guestbook_index'),
    path('sign/', views.sign, name='guestbook_sign')
]
