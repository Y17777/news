from django.urls import path
from .views import (NewsList, NewsDetail, PostCreate, Search, NewsUtil, PostEdit, PostDelete)


urlpatterns = [
     path('', NewsList.as_view(), name='news'),
     path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
     path('create/', PostCreate.as_view(), name='create_page'),
     path('search/', Search.as_view(), name='search_page'),
     path('utils/', NewsUtil.as_view(), name='news_util'),
     path('edit/<int:pk>', PostEdit.as_view(), name='edit_page'),
     path('delete/<int:pk>', PostDelete.as_view(), name='delete_page'),
]
