from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Contact'