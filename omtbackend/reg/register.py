from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(View):
    
    def get(self, request):
        return render(request, 'reg/page-register.html')
    
    def post(self, request):
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        ward = request.POST.get('ward')
        password = request.POST.get('password')
        password1 = request.POST.get('password2')
        account_type = request.POST.get('account_type')

        # Validate required fields
        if not all([fullname, username, email, phone, password, password1, state, ward]):
            return JsonResponse({'error': 'Please fill all the form fields'}, status=400)
        
        # Validate password match
        if password != password1:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        
        # Check if the email, username, or phone already exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        if User.objects.filter(phone=phone).exists():
            return JsonResponse({'error': 'Phone number already exists'}, status=400)
        
        # Create the user
        user = User.objects.create(
            fullname=fullname,
            username=username,
            email=email,
            phone=phone,
            state=state,
            ward=ward,
            password=make_password(password),
            account_type=account_type,
        )
        
        
        return JsonResponse({'success': 'User registered successfully!'}, status=200)
