from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def index(request):
    string = u'变量string'
    list = map(str, range(30))
    return render(request, 'learn/index.html', {'string': string, 'list': list})

def add(request):
    a, b= request.GET['a'], request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(c)

def add2(request, a, b):
    c = int(a)+int(b)
    return HttpResponse(c)
