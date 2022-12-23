from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                return redirect('acceuil')
            messages.error(request, 'Invalid credentials, try again')
            return render(request, 'authentication/login.html')
        messages.error(request, 'username and password must not be empty')
        return render(request, 'authentication/login.html')
    

class LogoutView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')