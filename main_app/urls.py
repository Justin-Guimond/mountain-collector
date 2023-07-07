from django.urls import path
from . import views

urlpatterns = [   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mountains/', views.mountains_index, name='index'),
    path('mountains/<int:mountain_id>/', views.mountains_detail, name='detail'),
    path('mountains/create/', views.MountainCreate.as_view(), name='mountains_create'),
    path('mountains/<int:pk>/update/', views.MountainUpdate.as_view(), name='mountains_update'),
    path('mountains/<int:pk>/delete/', views.MountainDelete.as_view(), name='mountains_delete'),
]