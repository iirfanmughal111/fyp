from cgitb import reset
from re import template
from django.urls import path,include
from .import views

#for main admin
from django.contrib.auth.urls import views as auth_views



urlpatterns = [
    path('contact_us',views.contact_us,name='contact_us'),

    # main_Admin paths
    path('main_admin',views.main_admin,name='main_admin'),
    path('export_user_csv',views.export_user_csv,name='export_user_csv'),
    path('user_change/<int:user_id>',views.user_change,name='user_change'),
    path('delete_user/<str:user_name>',views.delete_user,name='delete_user'),
    path('add_new_user',views.Add_New_User,name='add_new_user'),
    path('test',views.test,name='test'),
    path('add_device',views.add_device,name='add_device'),
    # path('add_device',views.add_device,name='add_device'),



    # path('account/',include('django.contrib.auth.urls')),
    # path('account/change_password',auth_views.PasswordChangeView.as_view()),






]
