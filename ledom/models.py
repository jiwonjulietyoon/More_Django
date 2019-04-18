from django.db import models
from django_extensions.db.models import TimeStampedModel # created_at, updated_at 자동으로 관리

# Create your models here.
class Student(TimeStampedModel):  # TimeStampedModel 별도로 created_at, updated_at 지정하지 않아도 됨
    name = models.CharField(max_length=10, unique=True)


class Article(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey(Student, on_delete=models.CASCADE)  # 변수 이름: student => writer (더 직관적으로. the "author" of the article)


class Comment(TimeStampedModel):
    content = models.CharField(max_length=140)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

