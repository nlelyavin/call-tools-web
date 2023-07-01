from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, ForeignKey, CASCADE

from app.models.base import BaseModel

is_archived_choices = [
    (0, '0'),
    (1, '1'),
]


class Token(BaseModel):
    """Токен аутентификации"""

    user = ForeignKey(User, on_delete=CASCADE, verbose_name='Пользователь')

    # Длина токена зависит от используемого алгоритма
    token = CharField(verbose_name='Токен', max_length=64)

    expired_date = DateTimeField(verbose_name='Дата истечения токена')
    is_archived = CharField(choices=is_archived_choices, default='0', max_length=2, verbose_name='Архивирован ли токен')
