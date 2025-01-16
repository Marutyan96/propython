from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm,ProfileUpdateForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend


def account_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')

            # Проверка наличия профиля
            try:
                profile = Profile.objects.get(user=user)
                return redirect('profile')  # Перенаправление на страницу профиля
            except Profile.DoesNotExist:
                messages.error(request, "Профиль не найден. Пожалуйста, создайте профиль.")
                return redirect('account_signup')  # Перенаправление на страницу регистрации
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    
    return render(request, 'account/login.html')

import logging

logger = logging.getLogger(__name__)

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('account_signup')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        profile_picture = request.FILES.get('profile_picture')

        logger.info(f"Updating profile for {request.user.username}: name={name}, profile_picture={profile_picture}")

        profile.name = name
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()
        
        messages.success(request, 'Профиль успешно обновлен!')
        return redirect('profile')

    return render(request, 'account/profile.html', {'profile': profile})


def account_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Создание профиля для нового пользователя
            Profile.objects.create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('profile')  # Перенаправление на страницу профиля
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SignUpForm()

    return render(request, 'account/account_signup.html', {'form': form})

