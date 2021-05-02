from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login 
from .models import Product
# Create your views here.

def index(request):
    product_objects = Product.objects.all()
    print(product_objects[0].title)
    print(product_objects[0].price)
    
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title_icontains=item_name)
        

    return render(request,'shop/index.html',{'product_objects':product_objects})

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