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

# 投稿できた形


def new(request):
  if request.method == 'POST':
    msg = testapp_text.objects.create(test_text=request.POST['word'])
    msg.save()
    return redirect(to="/testapp")
  return render(request, 'testapp/new.html')



# 最初やろうとしてた形
# def create(request):
#   # 投稿処理を書く
#   msg = request.POST['word']
#   # 終わったら投稿完了ページ
#   return render(request, 'testapp/new.html', msg)


# # 原文
# from django.shortcuts import render, redirect
# from .models import Message_bord

# def myapp_index(request):
#   msg = request.GET.get('words')
#   if msg is None:
#     data_list = Message_bord.objects.all()
#     contexts = {
#       'result_list': data_list,
#     }
#     return render(request, 'myapp/index.html', contexts)
#   else:
#     message_data = Message_bord()
#     message_data.new_message = msg
#     message_data.save()
#     data_list = Message_bord.objects.all()
#     contexts = {
#       'result_list': data_list,
#     }
#     return render(request, 'myapp/index.html', contexts)



# # 原文、修正版
# from django.shortcuts import render, redirect
# from .models import Message_bord

# def myapp_index(request):
#   msg = request.GET.get('words')
#   if msg is None:
#     data_list = Message_bord.objects.all()
#     contexts = {
#       'result_list': data_list,
#     }
#     return render(request, 'myapp/index.html', contexts)
#   else:
#     message_data = Message_bord()
#     message_data.new_message = msg
#     message_data.save()
#     data_list = Message_bord.objects.all()
#     contexts = {
#       'result_list': data_list,
#     }
#     return render(request, 'myapp/index.html', contexts)

