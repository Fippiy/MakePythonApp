from django.shortcuts import render
from django.http import HttpResponse
from .models import nekotter_text

# def index(request):
#   return HttpResponse('<p>Nekotter!</p>')

def index(request):
  tweet_list = nekotter_text.objects.all()
  context = {
  'lists': tweet_list,
  }
  return render(request, 'nekotter/index.html', context)
