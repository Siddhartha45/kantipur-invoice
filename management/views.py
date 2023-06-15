from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.views import View
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
def register(request):
    form= CreateUserForm()
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save(  )
            user=form.cleaned_data.get('username')
            messages.success(request,'Account is created'+user)
            return redirect('login')
        else:
            return HttpResponse("not valid data")
    context={'forms':form}
    

    return render(request,'register.html',context)


def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = CreateUserForm()
	return render(request, 'login.html', {'form':form, 'title':'log in'})


def ResetPassword(request):
    context={}
    return render(request,'reset.html',context)

@login_required
def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("login")

@login_required
def Customer(request):
    data = {
        's': commons.SALUTATION_CHOICES,
        'c':commons.CURRENCY_CHOICES,
    }
    if request.method=='POST':
        fm=AddCUstomerForm(request.POST)
        if fm.is_valid():
            cleaned_data = fm.cleaned_data
            AddCustomer.objects.create(**cleaned_data)
            return HttpResponse("saved")
    else:
        fm=AddCUstomerForm()
    context={'forms':fm, 'data': data}
    return render(request,'index.html',context)


def InvoiceView(request):
    if request.method=='POST':
        fm=InvoiceForm(request.POST)
        if fm.is_valid():
            fm.save()
            
    else:
        fm=InvoiceForm()
    context={'forms':fm}
    return render(request,'',context)


# def index(request):
#     return render(request,'index.html')


def update_data(request,id):
    dl=AddCustomer.objects.get(pk=id)

    if request.method=='POST':   
        if fm.is_valid():
            cleaned_data = fm.cleaned_data
            AddCustomer.objects.create(**cleaned_data)
            return HttpResponse("saved")
    else:
        fm=AddCUstomerForm(initial={
            'first_name': dl.first_name,
            'last_name': dl.last_name,
            'company_name': dl.company_name,
            'customer_display_name': dl.customer_display_name,
            'individual_name': dl.individual_name,
            'email': dl.email,
            'phone': dl.phone,
            'mobile': dl.mobile,
            })
    context={'forms':fm, 'dl':dl}   
    return render(request,'edit.html',context)
    
    
def Delete_table(request,id):
    if request.method=='POST':
        pi=AddCustomer.objects.get(pk=id)
        pi.delete()
        
        return HttpResponse('/')
    