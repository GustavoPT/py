from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})

    
def search(request):
    return render(request, "search.html",{})
def digitrecognizer(request):
    return render(request, "digitrecognizer.html",{})
def chat(request):
    return render(request,'chat.html',{})