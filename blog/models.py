from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib import admin
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, ItemBase

# Create your models here.


class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'P', 'Published'



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish = models.DateTimeField()
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices,default=Status.DRAFT)
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)