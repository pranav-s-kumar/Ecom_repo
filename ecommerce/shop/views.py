
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import Product, Category

# Create your views here.
def home(request,slug_c=None):
    page_c=None
    if slug_c!=None:
        page_c=get_object_or_404(Category,slug=slug_c)
        product=Product.objects.all().filter(category=page_c,available=True)
    else:
        product=Product.objects.all().filter(available=True)
    return render(request,'home.html',{'category':page_c,'product':product})

def prod_detail(request,slug_c,slug_p):
    try:
       product=Product.objects.get(category__slug=slug_c,slug=slug_p)
    except Exception as e:
        raise e
    return render(request,'products.html',{'product':product})

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()
        return redirect('signin')
    return render(request,'signup.html')


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username, password=password1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'demo_user.html',{'fname':fname})
        else:
            messages.error(request,'invalid credentials')
            return redirect('home')
    
    return render(request,'signin.html')


def signout(request):
    logout(request)
    return redirect('home')