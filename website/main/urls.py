from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('pictures/',views.pictures),
    path('about-us/',views.about),
]
