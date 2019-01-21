from django.shortcuts import render, redirect
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

def new(request):
  if request.method == 'POST':
    msg = nekotter_text.objects.create(tweet=request.POST['word'])
    msg.save()
    return redirect(to="/nekotter")
  return render(request, 'nekotter/new.html')
