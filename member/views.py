import email
import imp
from operator import imod
from sre_constants import SUCCESS
import django
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from . forms import RegisterUserForm
from django.contrib.auth.views import PasswordChangeView

# For js parsing
from json import  dumps


# Create your views here.




def index(request):
    c=30
    t=40
    v= 10 
    p =80
    l = 50
    data = {'c':c,'t':t,'v':v,'p':p,'l':l}
    datajson = dumps(data)
    return render(request,'member/index.html',{'data':datajson})

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('member_home')      
        else:
            messages.success(request,'Inavalid username/password. \n If you have account, please check your username and passowrd otherwise create your account first')
            return redirect('login_user')

        # Return an 'invalid login' error message.
            
    else:        
        return render(request,'member/login.html',{})

def logout_user(request):
    # Restrict to non-signedIn user
    if not request.user.is_authenticated:
        return render(request, 'member/login.html')
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('member_home')
    return render(request,'member/logout.html')        

def register_user(request):
    if request.method=='POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            djusername = form.cleaned_data['username']
            djpassword = form.cleaned_data['password1']
            djemail = form.cleaned_data['email']
            djf_name = form.cleaned_data['first_name']
            djl_name = form.cleaned_data['last_name']
            
            user = authenticate(username = djusername, password= djpassword, email = djemail, first_name = djf_name, last_name = djl_name )
            # user = authenticate(username= djusername,password=djpassword)
            login(request,user)
            print(user)
            print(form)
            messages.success(request, 'Successfully registered and loged in')
            return redirect('member_home')

    else:
        form = RegisterUserForm()        
    return render (request,'member/register.html' ,{'form':form})   


def change_password(PasswordChangeView):
    if not PasswordChangeView.user.is_authenticated:
        return render(PasswordChangeView, 'member/login.html')
    form_class = PasswordChangeForm
    Success_url = reverse_lazy('dashbord_user')

    # return render(request,'member/change_password.html',{})
    

def dashbord_user(request):
    # Restict to logout users
    if not request.user.is_authenticated:
        return render(request, 'member/login.html')
    return render(request,'member/dashbord.html',{})    
   