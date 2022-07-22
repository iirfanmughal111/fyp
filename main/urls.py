from cgitb import reset
from re import template
from django.urls import path,include
from .import views

#for main admin
from django.contrib.auth.urls import views as auth_views



urlpatterns = [
    path('contact_us',views.contact_us,name='contact_us'),
    path('',views.index,name='indexHome'),

    # main_Admin paths
    path('main_admin',views.main_admin,name='main_admin'),
    path('export_user_csv',views.export_user_csv,name='export_user_csv'),
    path('user_change/<str:user_name>',views.user_change,name='user_change'),
    path('delete_user',views.delete_user,name='delete_user'),
    path('add_new_user',views.Add_New_User,name='add_new_user'),
    path('add_device',views.add_device,name='add_device'),
    path('delete_device',views.delete_device,name='delete_device'),
    path('loadmoreUser',views.load_more_Users,name='loadmoreUser'),




    # path('account/',include('django.contrib.auth.urls')),
    # path('account/change_password',auth_views.PasswordChangeView.as_view()),
    path('test',views.test,name='test'),





]
