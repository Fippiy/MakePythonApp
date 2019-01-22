from django.contrib import admin
from .models import pictweet_tweet

class Add_Tweet(admin.ModelAdmin):
  list_display = ('id', 'name', 'text', 'image', 'date_time', 'user_id')

admin.site.register(pictweet_tweet, Add_Tweet)
