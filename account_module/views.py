from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from account_module.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from utils.email_service import send_email
from .models import User


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account_module/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error(field='email', error='ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(username=user_email, email=user_email, email_active_code=get_random_string(72), is_active=False)
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('accounts:login_page'))
        return render(request, 'account_module/register.html', {'register_form': register_form})


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('accounts:login_page'))
            else:
                # todo: show your account was activated message to user
                pass
        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account_module/login.html', {'login_form': login_form})

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('users:user_panel_dashboard'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
        return render(request, 'account_module/login.html', {'login_form': login_form})


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        return render(request, 'account_module/forgot_password.html', {'forget_pass_form': forget_pass_form})

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('home:home_page'))
        return render(request, 'account_module/forgot_password.html', {'forget_pass_form': forget_pass_form})


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('accounts:login_page'))
        reset_pass_form = ResetPasswordForm()
        return render(request, 'account_module/reset_password.html', {'reset_pass_form': reset_pass_form, 'user': user})

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('accounts:login_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('home:home_page'))
        return render(request, 'account_module/reset_password.html', {'reset_pass_form': reset_pass_form, 'user': user})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('accounts:login_page'))
