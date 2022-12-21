from django.db import models
from django.urls import reverse


class MyProject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Projects')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name="Project's content")
    site_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    link = models.CharField( max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return

    class Meta:
        verbose_name = 'My project'
        verbose_name_plural = 'My projects'
        ordering = ['-time_create']
