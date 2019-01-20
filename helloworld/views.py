from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import Add_Word

# def index(request):
#   return HttpResponse('<p>HelloWorld!</p>')

def index(request):
  data_list = Add_Word.objects.all()
  # template = loader.get_template('helloworld/index.html')
  context = {
  'lists': data_list,
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'helloworld/index.html', context)
