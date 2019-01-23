# ログイン関連
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
class SignUpView(generic.CreateView):
      form_class = UserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'accounts/signup.html'

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import pictweet_tweet
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth import get_user_model
# def index(request):
#   return HttpResponse('<p>test</p>')

def index(request):
  tweet_list = pictweet_tweet.objects.all().order_by('id').reverse()
  # UserModel = get_user_model()
  # user_list = Article.objects.all()
  # context = {
  # 'lists': tweet_list,
  # 'users': UserModel,
  # }
  context = {
    'lists': tweet_list
  }
  return render(request, 'pictweet/index.html', context)

def new(request):
  if request.method == 'POST':
    msg = pictweet_tweet.objects.create(
      name=request.POST['name'],
      text=request.POST['text'],
      image=request.POST['image'],
      date_time=timezone.datetime.now(),
      user_id = request.user.id
      )
    msg.save()
    return redirect(to="/pictweet")
  return render(request, 'pictweet/new.html')

def mypage(request,num):
  tweet_lists = pictweet_tweet.objects.all().filter(user_id=num)
  userinfo = User.objects.all().filter(id=num)
  context = {
    'lists': tweet_lists,
    'userinfo': userinfo
  }
  return render(request, 'pictweet/mypage.html', context)

def delete(request,num):
  pictweet_tweet.objects.filter(id=num).delete()
  return redirect(to="/pictweet")

def edit(request,num):
  if request.method == 'POST':
    msg = pictweet_tweet.objects.create(
      name=request.POST['name'],
      text=request.POST['text'],
      image=request.POST['image'],
      date_time=timezone.datetime.now(),
      user_id = request.user.id
      )
    msg.save()
    return redirect(to="/pictweet")
  tweet = pictweet_tweet.objects.filter(id=num)
  context = {
    'tweets': tweet,
  }
  return render(request, 'pictweet/edit.html', context)

def show(request,num):
  tweet = pictweet_tweet.objects.filter(id=num)
  context = {
  'lists': tweet,
  }
  return render(request, 'pictweet/index.html', context)

def redirect_top(request):
  return redirect(to="/pictweet")
  # return HttpResponse('<p>error</p>')
