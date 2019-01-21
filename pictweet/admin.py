from django.contrib import admin
from .models import pictweet_tweet

class Add_Tweet(admin.ModelAdmin):
  list_display = ('id', 'name', 'text', 'image', 'date_time')

admin.site.register(pictweet_tweet, Add_Tweet)

  # name = models.TextField()
  # text = models.TextField()
  # image = models.TextField()
  # date_time = models.DateTimeField()
