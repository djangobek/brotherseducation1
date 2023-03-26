from django import forms
from django.forms import ModelForm
from .models import *
class BlogForm(ModelForm):
    class Meta:
        model = MyfutureForm
        fields = ('ism_familyangiz','Telefon_raqamingiz','Qaysi_kursga_yozilmoqchisiz')
        widgets = {
            'ism_familyangiz': forms.TextInput(attrs={'class':'form-control item'}),
            'Telefon_raqamingiz': forms.TextInput(attrs={'class':'form-control item'}),
            'Qaysi_kursga_yozilmoqchisiz':forms.Select(attrs={'class':'form-control item'}),
        }
class Feedbakform(ModelForm):
    class Meta:
        model = Feedbacks
        fields = ('id','name','surname','phone_number','message')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control item', 'placeholder':'ism'}),
            'surname' : forms.TextInput(attrs={'class': 'form-control item', 'placeholder':'familya'}),
            'phone_number' : forms.TextInput(attrs={'class': 'form-control item', 'placeholder':'nomer'}),
            'message' : forms.Textarea(attrs={'class': 'form-control item', 'placeholder':'izoh'}),
        }

