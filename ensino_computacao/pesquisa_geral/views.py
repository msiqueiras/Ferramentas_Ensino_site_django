
from django.shortcuts import render
from django.http import HttpResponse

def pesquisa(request):
    return render(request, 'index.html', context=None)

    


