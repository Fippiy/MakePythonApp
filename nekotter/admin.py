from django.contrib import admin
from .models import nekotter_text

class Add_nekotter(admin.ModelAdmin):
  list_display = ('id', 'tweet')

admin.site.register(nekotter_text, Add_nekotter)
