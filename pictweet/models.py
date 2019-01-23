# from django.contrib.auth import get_user_model
from django.db import models

class pictweet_tweet(models.Model):
  name = models.TextField()
  text = models.TextField()
  image = models.TextField()
  date_time = models.DateTimeField()
  user_id = models.IntegerField(null=True)
  # user_id = models.ForeignKey(
  #     'user',
  #     on_delete=models.CASCADE,
  #   )

# class Article(models.Model):
#   testid = models.ForeignKey(
#       get_user_model(),
#       on_delete=models.CASCADE,
#     )
