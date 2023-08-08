from django.shortcuts import render
from .models import  Image ,Hero ,About ,Team , Blog
from .forms import RegisterForm , EmailForm 
# Create your views0 here.





def home(request):
    # ind = index.objects.first()
    # context = {
    #     'main':ind,
    # }
    
    H = Hero.objects.first()
    A = About.objects.first()
    T = Team.objects.first()
    
    form = RegisterForm(request.POST )
    form1 = EmailForm(request.POST)
    
    
    blog = Blog.objects.all()
    
    if form.is_valid():
        form.save()
    
    if form1.is_valid():
        form1.save()
    
        
    context = {
        'form':form,
        'form1':form1,
        'h':H,
        'a':A,
        't':T,
        'blog':blog
    }
    
    
    return render(request , 'index.html' , context)

def search(request):
    query = request.GET.get('q','')
    if query:
        results = Blog.objects.filter(title__icontains=query)
    else:
        results = []
        
    return render(request, 'search_results.html',{'results':results})














def doctor(request):
    return render(request , 'doctor.html')


def about(request):
    img = Image.objects.first()
    context = {
        'img':img
    }
    return render(request , 'about.html', context)


def contact(request):
    return render(request , 'contact.html')

def testimonial(request):
    return render(request , 'testimonial.html')

def treatment(request):
    return render(request , 'treatment.html')

def readMore(request , b_id):
    blog = Blog.objects.get(pk=b_id)
    context = {
        'blog':blog
    }
    return render(request , 'blog.html' , context)