from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bunnies/', views.bunnies_index, name='index'),
    path('bunnies/<int:bunny_id>/', views.bunnies_detail, name='detail'),
    path('bunnies/create/', views.BunnyCreate.as_view(), name='bunnies_create'),
    path('bunnies/<int:pk>/update/', views.BunnyUpdate.as_view(), name='bunnies_update'),
    path('bunnies/<int:pk>/delete/', views.BunnyDelete.as_view(), name='bunnies_delete'),
    path('bunnies/<int:bunny_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('bunnies/<int:bunny_id>/remove_toy/<int:toy_id>/',
         views.remove_toy, name='remove_toy'),
    path('bunnies/<int:bunny_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
    path('bunnies/<int:bunny_id>/add_photo/', views.add_photo, name='add_photo'),

]
