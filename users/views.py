from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
                            

from .utils import validate_email_address

# Create your views here.

class AcceuilView(View):
    def get(self, request):
        return render(request, 'users/acceuil.html')

class UpdateUserView(View):
    def get(self, request):
        return render(request, 'users/update_user.html')

    def post(selef, request):
        email = request.POST.get('email')
        if not validate_email_address(email):
            messages.error(request, 'Please enter a valid email address')
            return render(request, 'users/update_user.html')
        try:
            user = User.objects.get(username=request.user)
            user.email = email
            user.save()
            return render(request, 'users/acceuil.html', context={'email': user.email})
        except Exception as e:
            messages.error(request,'Error: %s, please try again' % str(e))
            return render(request, 'users/update_user.html')