from django.shortcuts import render, redirect
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

def new(request):
  # msg = request.POST['word']
  if request.method == 'POST':
    msg = testapp_text.objects.create(test_text=request.POST['word'])
    msg.save()
    return redirect(to="/testapp")
  # 新規投稿画面をだす
  # フォームを表示
  return render(request, 'testapp/new.html')

# def create(request):
#   # 投稿処理を書く
#   msg = request.POST['word']
#   # 終わったら投稿完了ページ
#   return render(request, 'testapp/new.html', msg)
