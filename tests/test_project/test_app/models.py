from django.db import models


class TestModel(models.Model):

    name = models.CharField(max_length=63, unique=True, verbose_name='Name')
    image = models.ImageField(verbose_name='Image', upload_to='uploads/')
