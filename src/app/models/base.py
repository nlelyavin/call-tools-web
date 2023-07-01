from django.db import models


class BaseModel(models.Model):
    """Базовая модель для всех классов"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # def to_dict(self) -> dict:
    #     print(self._meta.fields)
    #     return {field.name: getattr(self, field.name) for field in self._meta.fields}
