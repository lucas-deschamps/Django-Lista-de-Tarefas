from django.db import models

class Lista(models.Model):
    item = models.CharField(max_length=200)
    completo = models.BooleanField(default=False)

    def __str__(self):
        return self.item