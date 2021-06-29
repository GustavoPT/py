from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login 
from .models import Product
# Create your views here.
from django.core.paginator import Paginator


# test out the security 
# make my own password hash function
#  crwate cart from request 
#  cart form from model 
#  user from request 
#  user form from model 
#  list view for users 
#  detail view for users 

def index(request):
    product_objects = Product.objects.all()
    print(product_objects[0].title)
    print(product_objects[0].price)
    
    item_name = request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        print("here")
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
   
    page = request.GET.get('page')

    product_objects = paginator.get_page(page)
    return render(request,'shop/index.html',{'product_objects':product_objects})

def rating(request):








    return render(request,'rating.html',{})


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