from django.urls import path
from .views import (NewsList, NewsDetail, create_post, Search, news_util, edit_page, delete_page)


urlpatterns = [
     path('', NewsList.as_view()),
     path('<int:pk>', NewsDetail.as_view()),
     path('create/', create_post, name='post_create'),
     path('search/', Search.as_view()),
     path('utils/', news_util, name='news_util'),
     path('edit/<int:pk>', edit_page, name='edit_page'),
     path('delete/<int:pk>', delete_page, name='delete_page'),
]
