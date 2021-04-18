from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login 
from django.views.generic.list import ListView
# Create your views here.

def index(request):

    # 
    if request.user.is_authenticated:
        return render(request,'index.html',{})
    else:
        return redirect('register')

def cards(request):
    return render(request,'cards.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = form = UserCreationForm()
    context = {'form' : form}
    return render(request,'registration/register.html',context)