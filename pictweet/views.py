from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import pictweet_tweet

def index(request):
  return HttpResponse('<p>test</p>')

def index(request):
  tweet_list = pictweet_tweet.objects.all()
  context = {
  'lists': tweet_list,
  }
  return render(request, 'pictweet/index.html', context)

# def new(request):
#   if request.method == 'POST':
#     msg = nekotter_text.objects.create(tweet=request.POST['word'])
#     msg.save()
#     return redirect(to="/nekotter")
#   return render(request, 'nekotter/new.html')
