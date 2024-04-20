from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #Post es un modelo de Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #chardfield número limitado de caracteres
    text = models.TextField() #texto largo sin límite
    created_date = models.DateTimeField( #fecha y hora.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title