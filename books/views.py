from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'index.html')

def main(request):
    return render(request , 'main.html')