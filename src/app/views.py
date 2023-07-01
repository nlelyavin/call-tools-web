from django.http import JsonResponse
from django.views.generic import View

from app.constants import OBJECT_NOT_FOUND
from app.service import get_article_with_comments, get_articles_by_page


class ArticleView(View):
    """View описывающая CRUD для модели Article"""

    def get(self, request, pk, *args, **kwargs):
        """Получение статьи с комментариями"""

        article, comments = None, None

        if pk:
            article, comments = get_article_with_comments(article_id=pk)

        if article:
            result = JsonResponse({'article': article, 'comments': comments})
        else:
            result = JsonResponse(OBJECT_NOT_FOUND, status=404)

        return result

    def post(self, request, *args, **kwargs):
        ...


class ArticlesView(View):
    """View для работы со списком Article"""

    def get(self, request, *args, **kwargs):
        """Получение статей по заданной странице"""

        # Ищем все статьи (Постранично)
        page = request.GET.get('page', 1)
        articles = get_articles_by_page(page=page)

        if articles:
            result = JsonResponse({'articles': articles})
        else:
            result = JsonResponse(OBJECT_NOT_FOUND, status=404)

        return result
