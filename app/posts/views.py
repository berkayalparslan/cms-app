from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world, this is my first post')
