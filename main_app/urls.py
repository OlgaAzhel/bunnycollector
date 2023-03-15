from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bunnies/', views.bunnies_index, name='index'),
    path('bunnies/<int:bunny_id>', views.bunnies_detail, name='detail'),

]
