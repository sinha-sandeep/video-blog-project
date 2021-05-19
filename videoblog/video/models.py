from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from video.validators import file_size
from django.core import validators
from django import forms



# Create your models here.







class Video(models.Model):
#    STATUS_CHOICE=(('draft', 'Draft'), ('published', 'Published'))
    title=models.CharField(max_length=256)
#    slug=models.SlugField(max_length=256, unique_for_date="publish")
    auther=models.ForeignKey(User, models.CASCADE, related_name="video_post")

#    created=models.DateTimeField(auto_now_add=True)
#    updated=models.DateTimeField(auto_now=True)
#    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    publish=models.DateTimeField(default=timezone.now)
    videos=models.FileField(upload_to="video/%y",validators=[file_size])

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title
