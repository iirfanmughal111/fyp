from cgitb import reset
from re import template
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login_user',views.login_user,name='login_user'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('register_user',views.register_user,name='regiter_user'),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='member/change_password.html')),
    path('dashbord',views.dashbord_user,name='dashbord_user'),

    #Forgot Password links
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'authentication/reset_password.html'), name= 'reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name = 'authentication/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name= 'password_reset_confirm'),
    path('reset_passowrd_complete',auth_views.PasswordResetView.as_view(), name = 'password_reset_complete'),

    path('',views.index,name='member_home')


]
