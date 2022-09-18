from django.urls import path, include

from . import views
app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index, name = 'index'),
    # Страницы сообществ
    path('group/<slug:slug>/', views.group_posts, name ='group_posts'),
] 