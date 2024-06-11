from django.urls import path
from .views import NewsList, NewsDetail, search_news, NewsCreate, NewsEdit, NewsDelete, ArticleEdit, ArticleCreate, ArticleDelete

urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/search/', search_news, name='search_news'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]