from django.http import HttpResponse

def index(request):
    return HttpResponse("🏀 スタッツ管理ページへようこそ！")
