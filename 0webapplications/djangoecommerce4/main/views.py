from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login 
from .models import Product
# Create your views here.
from django.core.paginator import Paginator
from django.views.generic import ListView 

# test out the security 
# make my own password hash function
#  crwate cart from request 
#  cart form from model 
#  user from request 
#  user form from model 
#  list view for users 
#  detail view for users 



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

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



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Rating


def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context = {
        'object':obj
    }
    return render(request,'ratings/main.html',context)


# from .forms import ModelFormWithFileField

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})

def rating(request):


    obj = Rating.objects.get
    context = {}





    return render(request,'rating.html',{})


def login(request):
    return render()
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