from django.urls import path
from . import views  # This must be correct!

urlpatterns = [
    path('', views.index, name='index'),
    path('interest/', views.interest, name='interest'),
]