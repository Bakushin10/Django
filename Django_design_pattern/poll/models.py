from django.db import models

class User(models.Model):
  """
    the reason to use model is that it checks the value error here
  """
  name = models.CharField(max_length=10)

class NumList(models.Model):
  #num1 = models.IntegerField(default="", blank=False)
  #num2 = models.IntegerField(default="", blank=False)
  num1 = models.IntegerField(null=False, blank=False)
  num2 = models.IntegerField(null=False, blank=False)
  num3 = models.IntegerField(null=False, blank=False)

class Post(models.Model):
  title = models.CharField(max_length=10, blank=False)
  body = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  nums = models.ForeignKey(NumList, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)