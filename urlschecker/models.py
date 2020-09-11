from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class URL(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField()
    status_code = models.IntegerField(null=True, blank=True)

    class META:
        verbose_name_plural = "URL's"
