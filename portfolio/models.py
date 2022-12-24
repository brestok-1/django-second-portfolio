from django.db import models
from django.urls import reverse


class MyProject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Projects')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    url = models.CharField(max_length=255, blank=True, verbose_name='Project_url')
    description = models.TextField(verbose_name='Desription')
    issues = models.TextField(verbose_name='Issues')
    solve = models.TextField(verbose_name='Solution')
    time_create = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})

    class Meta:
        verbose_name = 'My project'
        verbose_name_plural = 'My projects'
        ordering = ['-time_create']


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    project = models.ForeignKey(MyProject, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)
