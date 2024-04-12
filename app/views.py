from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.db.utils import IntegrityError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Attempt to create the user
            data = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            data.save()
            return redirect('login')
        except IntegrityError:
            # Handle the case where the username is already taken
            return render(request, 'register.html', {'error': 'Username is already taken'})

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('deshboard')

    return render(request, 'login.html')

def deshboard(request):
    return render(request, 'deshboard.html') 

def about(request):
    return render(request, 'aboutme.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contactus.html')
