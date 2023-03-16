from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bunnies/', views.bunnies_index, name='index'),
    path('bunnies/<int:bunny_id>/', views.bunnies_detail, name='detail'),
    path('bunnies/create/', views.BunnyCreate.as_view(), name='bunnies_create'),
    path('bunnies/<int:pk>/update/',
         views.BunnyUpdate.as_view(), name='bunnies_update'),
    path('bunnies/<int:pk>/delete/',
         views.BunnyDelete.as_view(), name='bunnies_delete'),

]
