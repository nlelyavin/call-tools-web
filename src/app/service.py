"""Бизнес-логика приложения"""
import os
from typing import Optional

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage

from app.models import Article

PAGE_SIZE = os.environ.get('ARTICLE_PAGE_SIZE', 100)


def get_article(article_id: int) -> Optional[Article]:
    """Получение статьи по ее ID"""

    try:
        article = Article.objects.get(id=article_id)
        article = article.to_dict()
    except Article.DoesNotExist:
        article = None

    return article


def get_articles_by_page(page: int) -> list:
    """Получить все статьи по странице"""

    all_articles = Article.objects.values('title', 'text', 'author_id').order_by('-id')
    paginator = Paginator(all_articles, PAGE_SIZE)

    try:
        page_info = paginator.page(page)
    except EmptyPage:
        return list()

    return list(page_info)
