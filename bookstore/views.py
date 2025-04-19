from django.http import HttpResponse

def index(request):
    return HttpResponse("📚 書店ホームページへようこそ！")
