from django.contrib import admin
from .models import testapp_text

# admin.site.register(testapp_text)

class Add_testAdmin(admin.ModelAdmin):
  list_display = ('id', 'test_text')

admin.site.register(testapp_text, Add_testAdmin)
