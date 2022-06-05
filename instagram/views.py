from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.

def signup(request):
    if request.method == 'POST':
        return redirect('index')
    return render (request,'registration/signup.html')

def index (request):
    if request.method == 'POST':
        return HttpResponseRedirect(request.path_info)
    return render(request, 'instagram/index.html')

    
        
