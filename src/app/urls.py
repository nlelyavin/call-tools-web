from django.urls import path

from app.views import ArticlesView, ArticleView

urlpatterns = [
    path('articles', ArticlesView.as_view(), name='articles'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
]
