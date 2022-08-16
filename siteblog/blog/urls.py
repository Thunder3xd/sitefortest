from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('unique/', Unique.as_view(), name='unique'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]
