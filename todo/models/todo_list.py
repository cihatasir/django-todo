from django.db import models
from django.db.models.fields import CharField

class TodoModel(models.Model):
    title = models.CharField(max_length=25)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.title
