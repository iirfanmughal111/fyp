from distutils.command.build_scripts import first_line_re
import imp
from cupshelpers import Printer
from django.shortcuts import redirect, render
from requests import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from member.forms import RegisterUserForm
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
# from . models import contact_us_db

#For User model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from urllib3 import HTTPResponse



# Create your views here.
def contact_us(request):
    #   if request.method =='POST':
    #     djname = request.POST.get('name','')
    #     djemail = request.POST.get('email','')
    #     djphone = request.POST.get('phone','')
    #     djdesc = request.POST.get('desc','')
        # contact = contact_us_db(name=djname,email= djemail, phone= djphone, desc = djdesc)
        # contact.save()

    return render (request,'main/contact_us.html',{})
    

@login_required
def main_admin(request):
    if request.user.is_superuser:
        # Getting All user
        User = get_user_model()
        users = User.objects.all()
        
        # Adding new Users 
        if request.method!='POST':
            form = RegisterUserForm()   
        else:
            form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            djusername = form.cleaned_data['username']
            djpassword = form.cleaned_data['password1']
            djemail = form.cleaned_data['email']
            djf_name = form.cleaned_data['first_name']
            djl_name = form.cleaned_data['last_name']
            
            user = authenticate(username = djusername, password = djpassword, email = djemail, first_name = djf_name, last_name = djl_name )
            
        context = {'users':users,'form':form}
        return render (request,'main/main_admin.html',context)
    else:
        return render (request,'member/index.html')


def user_change(request,user_id):
    User  = get_user_model().objects.get(id=user_id)
    if request.method == 'POST':
        User.username  = request.POST.get('username')
        User.first_name  = request.POST.get('first_name')
        User.last_name  = request.POST.get('last_name')
        User.email  = request.POST.get('email')
        User.is_staff = True if request.POST.get("is_staff") == "on" else False
        User.is_active = True if request.POST.get("is_active") == "on" else False
        User.is_superuser = True if request.POST.get("is_superuser") == "on" else False


        # newPass = request.POST.get('password')
        # User.set_password(newPass)
        

        User.save()
       
   
    context = {'user':User}
    return render (request,'main/user_change.html',context)


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

# def save_user_change(request):
#     User  = get_user_model().objects.get(id=User.user_id)
#     print(User.username)
#     if request.method == 'POST':
#         dj_f_name  = request.POST.filter('first_name',instance = User)
#         dj_l_name  = request.POST.filter('last_name',instance = User)
#         save = get_user_model(first_name = dj_f_name,last_name = dj_l_name)
#         print(save.username)
#         save.save()
#         print(save.username)
#         print('sfjlsjflksf')
#         redirect('main_admin')


def export_user_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['username','first_name','last_name','email','password'])
        
    for user in User.objects.all().values_list('username','first_name','last_name','email','password'):
        writer.writerow(user)
        # print("printed users:")
        # print(user)
        # print(writer.writerow(user))
    response['Content-disposition'] = 'attachment; filename = "user.csv"'    
    return response

def delete_user(request,user_name):
    User  = get_user_model().objects.get(username=user_name)
    User.delete()
    # return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    return redirect('main_admin')


def Add_New_User(request):
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
            # login(request,user)
            messages.success(request, 'Successfully registered and loged in')
            return redirect('add_new_user')

    else:
        form = RegisterUserForm()        
    return render (request,'main/add_new_user.html' ,{'form':form})   
    