from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms 

class RegisterUserForm (UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2'}))

    class  Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
    def __init__(self, *args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,*kwargs)           
        self.fields['username'].widget.attrs['class'] = 'form-control my-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control my-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control my-2'
            
            


# class PasswordChangingform (PasswordChangeForm):
    # old_password = forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'form-control','type': 'password'} ))
    # new_password1 = forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    # new_password2 = forms.PasswordInput(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))

    # class  Meta:
    #     model = User
    #     fields = ('old_password','new_password1','new_password2',)
    # def __init__(self, *args,**kwargs):
    #     super(PasswordChangingform,self).__init__(*args,*kwargs)           
    #     self.fields['old_password'].widget.attrs['class'] = 'form-control my-2'
    #     self.fields['new_password1'].widget.attrs['class'] = 'form-control my-2'
    #     self.fields['new_password2'].widget.attrs['class'] = 'form-control my-2'   