from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('pictures/',views.pictures, name='pictures'),
    path('about-us/',views.about, name='about'),
    path('create/',views.create, name='create'),
    path('education/',views.education, name='education'),

]
