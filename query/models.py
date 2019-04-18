from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class User(TimeStampedModel):
    name = models.CharField(max_length=20, unique=True)

class Post(TimeStampedModel):
    title = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(TimeStampedModel):
    content = models.CharField(max_length=20, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


