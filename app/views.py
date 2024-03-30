from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is homepage")

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'aboutme.html')


def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contactus.html')