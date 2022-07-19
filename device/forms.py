from django import forms 
from django.core.validators import MaxValueValidator
from .models import devices
from traitlets import default


class DevicesForm (forms.Form):
    # device_id = forms.
    vehicle_no = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control my-2',}))
    route_name = forms.CharField(required=False,max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2'}))
    temperature = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2','required':'False'}))
    carbon_mono = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))
    humidity = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))
    light = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))
    noise = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))
    langitude = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))
    latitude = forms.BooleanField(required=False,initial= False,widget=forms.CheckboxInput(attrs={'class':'form-check-input my-2'}))


#  device_id  vehicle_no route_name  temperature carbon_mono  humidity light noise langitude latitude

    # class  Meta:
    #     model = devices
    #     fields = ['device_id','vehicle_no','route_name','temperature','carbon_mono','humidity','light','noise','langitude','latitude']
    
            
            
