from django.db import models


class Column(models.Model):
    height: float
    width: float

    class Meta:
        app_label = "app1"
