from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import pictweet_tweet

from django.contrib.auth.models import User, AnonymousUser

# def index(request):
#   return HttpResponse('<p>test</p>')

def index(request):
  tweet_list = pictweet_tweet.objects.all()
  context = {
  'lists': tweet_list,
  }
  return render(request, 'pictweet/index.html', context)

  # if request.user.is_authenticated():
  # if request.user == AnonymousUser():
  #   test = "test"
  # else:
  #   test = "test"


# def new(request):
#   if request.method == 'POST':
#     msg = nekotter_text.objects.create(tweet=request.POST['word'])
#     msg.save()
#     return redirect(to="/nekotter")
#   return render(request, 'nekotter/new.html')



from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
      form_class = UserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'accounts/signup.html'
