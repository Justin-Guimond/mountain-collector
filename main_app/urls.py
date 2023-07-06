from django.urls import path
from . import views

urlpatterns = [   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mountains/', views.mountains_index, name='index'),
    path('mountains/<int:mountain_id>/', views.mountains_detail, name='detail'),
]