from django.db import models

class pictweet_tweet(models.Model):
  name = models.TextField()
  text = models.TextField()
  image = models.TextField()
  date_time = models.DateTimeField()
  user_id = models.IntegerField(null=True)

