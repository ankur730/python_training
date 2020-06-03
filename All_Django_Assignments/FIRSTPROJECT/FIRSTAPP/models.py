from django.db import models

# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    contact = models.IntegerField()
    address = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Detail'


