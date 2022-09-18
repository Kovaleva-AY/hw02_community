from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("group_posts", kwargs={"slug": self.slug})


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(Group,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='groups'
                              )
