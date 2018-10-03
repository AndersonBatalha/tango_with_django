from django.db import models

from ..models import Category


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural='Pages'

    def __str__(self):
        return self.title
