"""Бизнес-логика приложения"""
import os
from typing import Optional

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Prefetch

from app.models import Article, Comment

PAGE_SIZE = os.environ.get('ARTICLE_PAGE_SIZE', 100)


def get_article_with_comments(article_id: int) -> (Optional[Article], Optional[list]):
    """Получение статьи по ее ID"""

    article = None
    comments = None
    comment_fields = ('created_at', 'text', 'article_id', 'author_id')

    # Как будет выглядеть запрос для получения комментариев (Здесь он еще не исполняется)
    comment_queryset = Comment.objects.only(*comment_fields)
    prefetch = Prefetch(lookup='comment_set', queryset=comment_queryset)

    try:
        article_and_comments = Article.objects.prefetch_related(prefetch).get(id=article_id)
    except Article.DoesNotExist:
        return article, comments

    article = article_and_comments.to_dict()
    comments = list(article_and_comments.comment_set.values(*comment_fields))

    return article, comments


def get_articles_by_page(page: int) -> list:
    """Получить все статьи по странице"""

    all_articles = Article.objects.values('title', 'text', 'author_id').order_by('-id')
    paginator = Paginator(all_articles, PAGE_SIZE)

    try:
        page_info = paginator.page(page)
    except EmptyPage:
        return list()
    print(page_info.object_list)
    return list(page_info)
