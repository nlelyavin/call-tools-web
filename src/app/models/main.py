from django.contrib.auth.models import User
from django.db.models import ForeignKey, CASCADE, CharField, TextField

from ..models.base import BaseModel


class Article(BaseModel):
    """Модель статьи"""

    author = ForeignKey(User, on_delete=CASCADE)

    title = CharField(max_length=150, verbose_name='Название статьи')
    text = TextField(max_length=4000, verbose_name='Текст статьи')

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'text': self.text}


class Comment(BaseModel):
    """Модель комментария в статье (Article)"""

    author = ForeignKey(User, on_delete=CASCADE)
    article = ForeignKey(Article, on_delete=CASCADE)

    text = CharField(max_length=4000, verbose_name='Текст комментария')
