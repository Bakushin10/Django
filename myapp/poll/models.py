from django.db import models

class User(models.Model):
  """
    the reason to use model is that it checks the value error here
  """
  name = models.CharField(max_length=10)

class Post(models.Model):
  title = models.CharField(max_length=128)
  body = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)