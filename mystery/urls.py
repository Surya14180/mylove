from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('puzzle1/', views.puzzle_level_1, name='puzzle_level_1'),
    path('puzzle2/', views.puzzle_level_2, name='puzzle_level_2'),
    path('puzzle3/', views.puzzle_level_3, name='puzzle_level_3'),
    path('reveal/', views.reveal_page, name='reveal_page'),
] 