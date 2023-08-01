from django import forms

from .models import Register

class RegisterForm(forms.ModelForm):
    
    
    class Meta:
        model = Register
        fields = ['name' , 'doctorName' ,'ahvol' , 'phoneNumber' , 'belgilar' , 'boshlangan']
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'doctorName': forms.TextInput(attrs={'class':'form-control'}),
            'ahvol': forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber': forms.NumberInput(attrs={'class':'form-control'}),
            'belgilar': forms.Textarea(attrs={'class':'form-control'}),
            'boshlangan': forms.DateInput(attrs={'type':'date','class':'form-control'})
        }