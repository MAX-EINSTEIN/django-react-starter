from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50, null=False)

    def clean(self) -> None:
        self.name = self.name.lower()
        return super().clean()

    def __str__(self):
        return self.name


class Post(models.Model):

    class PublishedPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    published_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=OPTIONS, default='published')
    slug = models.SlugField(max_length=200, unique_for_date='published_on')
    objects = models.Manager()  # default manager
    published_posts_objects = PublishedPostObjects()  # custom manager

    class Meta:
        ordering = ('-published_on', )

    def __str__(self):
        return self.title
