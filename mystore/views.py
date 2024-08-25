from django.shortcuts import render
from django.views import View
from.models import product,Cart
from django.db.models import Count
from.forms import CustomerRegistrationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from.forms import CustomerForm
from.models import Customer


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        products=product.objects.all()
        cartitems=Cart.objects.filter(user=request.user)
        totalitems=0
        for p in cartitems:
            totalitems+=1
    return render(request,"mystore/home.html",locals())


class categoryViews(View):
    def get(self,request,val):
        products= product.objects.filter(category=val) 
        return render(request,"mystore/category.html",{"products":products})
    
    
class Categorytitle(View):
    def get(self,request,val):
        product=product.objects.filter(title=val)
        title=product.objects.filter(category=product[0].categorey).values('title')
        return render(request,'mystore/category.html',locals())
    
    
class product_detail(View):
    def get (self,request,id):
        prod=product.objects.get(pk=id)
        return render(request,"mystore/product_detail.html",locals())
    
    
class aboutus(View):
    def get(self,request):
        return render (request,'mystore/aboutus.html')
    
    
class contactus(View):
    def get(self,request):
        return render (request,'mystore/contactus.html')
    
    
class Signup(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'mystore/CustomerRegistration.html',locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created. Please log in.')
            return redirect('/Login/')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'mystore/CustomerRegistration.html',locals())
    
    
class user_Login(View):
    def get(self,request):
        fm=AuthenticationForm()
        return render (request,"mystore/Login.html",locals())
    def post(self,request):
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                fm=AuthenticationForm()
            return render(request, 'mystore/CustomerRegistration.html',locals())
        

class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/Login/")
    
    
class Customerdetails(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'mystore/Customerdetails.html',locals())

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            fm=form.save(commit=False)
            fm.user=request.user
            fm.save()
            messages.success(request, 'Delaits submited.')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'mystore/Customerdetails.html',locals())
    

def address(request):
    Address=Customer.objects.filter(user=request.user)
    return render(request, 'mystore/address.html',{"Addresses":Address})


class update(View):
    def get(self,request,pk):
        user=Customer.objects.get(id=pk)
        fm=CustomerForm(instance=user)
        return render(request,'mystore/Customerdetails.html',{"form":fm})
    def post(self,request,pk):
        user=Customer.objects.get(id=pk)
        fm=CustomerForm(request.POST,instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('/address/')
        

def changepass(request):
    if request.method=='GET':
        fm=PasswordChangeForm(user=request.user)
        return render(request, "mystore/changepassword.html",{"form":fm})
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        


def add_to_cart(request,id):
    prod=product.objects.get(pk=id)
    Cartitem,created=Cart.objects.get_or_create(user=request.user,product=prod)
    if not created:
        Cartitem.quantity+=1
        Cartitem.save()
    else:
        Cartitem.save()
    return redirect('/Showcart/')


def showcart(request):
    products=Cart.objects.filter(user=request.user)
    totalitems=0
    amount=0
    for p in products:
        value= p.quantity*p.product.discounted_price
        amount=amount+value
        totalitems+=1
    totalamount=amount+40
    return render (request,'mystore/Cart.html',locals())


def plusitem(request,id):
    saman=Cart.objects.get(pk=id).quantity
    saman+=1
    Cart.objects.filter(pk=id).update(quantity=saman)
    return redirect ('/Showcart/')



def minusitem(request,id):
    saman=Cart.objects.get(pk=id).quantity
    if saman==1:
        Cart.objects.get(pk=id).delete()
    saman-=1
    Cart.objects.filter(pk=id).update(quantity=saman)
    
    return redirect ('/Showcart/')


def remove(request,id):
    Cart.objects.get(pk=id).delete()
    return redirect('/Showcart/')


def checkout(request):
    addresses=Customer.objects.filter(user= request.user)
    products=Cart.objects.filter(user=request.user)
    totalitems=0
    amount=0
    itemsincart=0
    for p in products:
        value= p.quantity*p.product.discounted_price
        amount=amount+value
        totalitems+=1
        itemsincart =+ p.quantity
    totalamount=amount+40

    
    return render(request,'mystore/checkout.html',locals())


