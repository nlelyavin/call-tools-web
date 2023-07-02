from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app.views import ArticlesView, ArticleView

# Можно было бы отключить CSRF на уровне MiddleWare (Зависит от того, как планируем использовать сервис)
urlpatterns = [
    path('articles', ArticlesView.as_view(), name='articles'),
    path('article/<int:pk>/', csrf_exempt(ArticleView.as_view()), name='article'),
    path('article/', csrf_exempt(ArticleView.as_view()), name='article'),
]
