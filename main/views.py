from distutils.command.build_scripts import first_line_re
from django.shortcuts import redirect, render
from requests import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from member.forms import RegisterUserForm
from device.forms import DevicesForm
from device.models import devices,sensors
from django.http import HttpResponse, JsonResponse
import csv
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# from . models import contact_us_db
from json import dumps
#For User model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from urllib3 import HTTPResponse
from django.core.paginator import Paginator,EmptyPage
from django.core import serializers



# Create your views here.

def index(request):

    return render (request,'main/index.html')


    

@login_required
def main_admin(request):
    if request.user.is_superuser:
        # Getting All user
        User = get_user_model()
        rev_users = User.objects.all().order_by('-id')
        users = Paginator(rev_users,15)
        page_list = request.GET.get('page')
        users=users.get_page(page_list)
        # users = User.objects.all().order_by('-id')[:15]
        print(users)
        totalUser = User.objects.all().count()
        # Adding new Users 
        # if request.method!='POST':
        #     form = RegisterUserForm()   
        # else:
        #     form = RegisterUserForm(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         djusername = form.cleaned_data['username']
        #         djpassword = form.cleaned_data['password1']
        #         djemail = form.cleaned_data['email']
        #         djf_name = form.cleaned_data['first_name']
        #         djl_name = form.cleaned_data['last_name']
                
        #         user = authenticate(username = djusername, password = djpassword, email = djemail, first_name = djf_name, last_name = djl_name )
            #UserRegistrationForm
        UserRegform = RegisterUserForm()
            # Device Form
        dev_form = DevicesForm()

        # AllDevicesList
        # alldevices = devices.objects.all() 
        rev_devices = devices.objects.all().order_by('-device_id')
        device_page = Paginator(rev_devices,15)
        page_list = request.GET.get('page')
        device_page = device_page.get_page(page_list)
        totaldevices = devices.objects.all().count()


            
       
    
            
           
        context = {'users':users,'UserRegform':UserRegform,'devices':device_page, 'deviceForm':dev_form,'totalUser':totalUser,'totaldevices':totaldevices}
        # context = {'users':users,'form':form,'devices':alldevices, }

        return render (request,'main/main_admin.html',context)
    else:
        return render (request,'member/index.html')

def Add_New_User(request):
    if request.method=='POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                djusername = form.cleaned_data['username']
                djemail = form.cleaned_data['email']
                djf_name = form.cleaned_data['first_name']
                djl_name = form.cleaned_data['last_name']
                djpassword = form.cleaned_data['password1']
                djpassword2 = form.cleaned_data['password2']      
                user = authenticate(username = djusername, password = djpassword, email = djemail, first_name = djf_name, last_name = djl_name,password2=djpassword2 )
                user.save()
                #alldevices = devices.objects.values()
                #devicesList = list(alldevices)
                users = User.objects.values().order_by('-id')[:15]
                userList15 = list(users)
            # user = authenticate(username= djusername,password=djpassword)
            # login(request,user)
            # messages.success(request, 'Successfully registered and loged in')
            return JsonResponse({'status':1,'usersList':userList15})

    else:
          return JsonResponse({'status':0})

def delete_user(request):
    if request.method=='POST':
        user = request.POST['username']
        del_user  = User.objects.get(username=user)
        users = User.objects.values().order_by('-id')[:15]
        userList15 = list(users)
    
        del_user.delete()
        return JsonResponse({'status':1,'usersList':userList15})

    else:
          return JsonResponse({'status':0})
  

def contact_us(request):
    #   if request.method =='POST':
    #     djname = request.POST.get('name','')
    #     djemail = request.POST.get('email','')
    #     djphone = request.POST.get('phone','')
    #     djdesc = request.POST.get('desc','')
        # contact = contact_us_db(name=djname,email= djemail, phone= djphone, desc = djdesc)
        # contact.save()

    return render (request,'main/contact_us.html',{})
def test(request):

            
        
    context = {'deviceForm'}
    # context = {'users':users,'form':form,'devices':alldevices, }

    return render (request,'main/test.html',context)


def add_device(request):
    if request.method=='POST':
        device_form = DevicesForm(request.POST)    
        if device_form.is_valid():
            # vehicle_no route_name  temperature carbon_mono  humidity light noise  langitude latitude
            dj_v_no = request.POST['vehicle_no']
            dj_r_name = request.POST['route_name']
            dj_temp = True if request.POST.get('temperature') == "on" else False
            dj_co = True if request.POST.get('carbon_mono') == "on" else False
            dj_hum = True if request.POST.get('humidity') == "on" else False
            dj_light = True if request.POST.get('light') == "on" else False
            dj_noise = True if request.POST.get('noise') == "on" else False
            dj_long = True if request.POST.get('latitude') == "on" else False
            dj_lat = True if request.POST.get('latitude') == "on" else False

            dev = devices(vehicle_no=dj_v_no, route_name = dj_r_name,  temperature= dj_temp, carbon_mono = dj_co,  humidity = dj_hum, light = dj_light,  noise = dj_noise, langitude = dj_long, latitude = dj_lat)
            dev.save()
            alldevices = devices.objects.values()
            devicesList = list(alldevices)
           
            return JsonResponse({'status':1,'devicesList':devicesList})
        else:
            return JsonResponse({'status':0})

def delete_device(request):
    if request.method=='POST':
        dj_dev_id = request.POST.get('dj_dev_id',False)
        del_dev  = devices.objects.get(device_id=dj_dev_id)
        del_dev.delete()
        alldevices = devices.objects.values()
        devicesList = list(alldevices)
        return JsonResponse({'status':1,'devicesList':devicesList})
    else:
        return JsonResponse({'status':0})
   
def load_more_Users(request):
    if request.method=='POST':
        offset = int(request.POST['offset'])
        limit = 10
        serial  = offset+limit
        total_users = User.objects.all().count()
        print(total_users)
        if offset>=total_users:
            return JsonResponse({'status':0,})
        else:
            allusers = User.objects.all().order_by('-id')[offset:offset+limit]         
            userList = serializers.serialize('json',allusers)
      
        return JsonResponse({'usersList':userList,'serial':serial})


def user_change(request,user_name):
    User  = get_user_model().objects.get(username=user_name)
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
            # print(user)
            # print(form)
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




    