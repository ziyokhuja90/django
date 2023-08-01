from django.shortcuts import render
# from .models import index  
from .forms import RegisterForm
# Create your views here.
def home(request):
    # ind = index.objects.first()
    # context = {
    #     'main':ind,
    # }
    
    form = RegisterForm(request.POST )
    
    if form.is_valid():
        form.save()
    
    context = {
        'form':form
    }
    return render(request , 'index.html' , context)

def doctor(request):
    return render(request , 'doctor.html')


def about(request):
    return render(request , 'about.html')


def contact(request):
    return render(request , 'contact.html')

def testimonial(request):
    return render(request , 'testimonial.html')

def treatment(request):
    return render(request , 'treatment.html')