from distutils.command.config import config
from django.db import models
from django.urls import reverse
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField 


class Post(models.Model):

    title = models.CharField(max_length=255, blank=False)
    body = RichTextUploadingField(config_name='awesome_ckeditor')

    def __str__(self):
        return self.title

    def get_absolute_url(self,):
        return reverse('post-detail',args=[self.id])