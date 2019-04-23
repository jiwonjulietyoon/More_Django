from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

# Create your models here.
class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lovers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="bookmarks")
        # 여기서 related_name을 명시하지 않으면, user.post가 두 가지를 의미하게 되어 (작성자인 user, 좋아요한 user) 중의적이다.