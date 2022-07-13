from django import forms 
from django.core.validators import MaxValueValidator
from traitlets import default


class DevicesForm (forms.Form):
    # device_id = forms.
    vehicle_no = forms.NumberInput()
    route_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    temperature = forms.BooleanField(initial= False)
    carbon_mono = forms.BooleanField(initial= False)
    humidity = forms.BooleanField(initial= False)
    light = forms.BooleanField(initial= False)
    noise = forms.BooleanField(initial= False)
    langitude = forms.BooleanField(initial= False)
    latitude = forms.BooleanField(initial= False)


   

    # class  Meta:
    #     model = User
    #     fields = ('username','email','first_name','last_name','password1','password2')
    # def __init__(self, *args,**kwargs):
    #     super(RegisterUserForm,self).__init__(*args,*kwargs)           
    #     self.fields['username'].widget.attrs['class'] = 'form-control my-2'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control my-2'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control my-2'
            
            
