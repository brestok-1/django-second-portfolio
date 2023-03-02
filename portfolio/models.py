import sys
from PIL import Image
from django.db import models
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile

from io import BytesIO


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
        ordering = ['-time_create', 'title']


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    name = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(MyProject, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        new_img_rgb = img.convert('RGB')
        resized_img = new_img_rgb.resize((1840, 911), Image.ANTIALIAS)
        filestream = BytesIO()
        resized_img.save(filestream, 'JPEG', quality=90)
        filestream.seek(0)
        name = self.image.name.split('.')[0]
        self.image = InMemoryUploadedFile(
            filestream, 'Image', name, 'jpeg/image', sys.getsizeof(filestream), None
        )
        super(ProjectImage, self).save(*args, **kwargs)


class MySkills(models.Model):
    skill = models.CharField(verbose_name='Skill', max_length=255)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'My Skill'
        verbose_name_plural = 'My Skills'
