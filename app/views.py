from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'chaitanya'}
    return render(request,'forloop.html',d)