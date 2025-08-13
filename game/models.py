from django.db import models


class ValidManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(answer=True)


class Word(models.Model):
    text = models.CharField(max_length=5, unique=True)
    answer = models.BooleanField()

    objects = models.Manager()
    valid = ValidManager()

    class Meta:
        ordering = ['text']

    def __str__(self):
        return f'{self.text}'
