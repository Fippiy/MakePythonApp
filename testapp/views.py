from django.shortcuts import render
from django.http import HttpResponse
from .models import testapp_text

# def index(request):
#   return HttpResponse('<p>HelloWorld!</p>')

def index(request):
  text_list = testapp_text.objects.all()
  # return HttpResponse(text_list)
  context = {
  'lists': text_list,
  }
  return render(request, 'testapp/index.html', context)
