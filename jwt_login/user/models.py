from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=150)
  nickname = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)

  class Meta:
    db_table = 'username'


class Article(models.Model):
  writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
  title = models.CharField(max_length=200)
  content = models.TextField()

  class Meta:
    db_table = 'title'