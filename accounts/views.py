from django.shortcuts import render
from django.contrib import messages
from tkinter import messagebox
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm#, LogInForm
from django.http import HttpResponseRedirect
from tkinter import messagebox

# Create your views here.
# @login_required
# def my_view(request):
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# class LogInView(generic.CreateView):
#     # form_class = LoginForm
#     template_name = "accounts/login.html"

def loginf(request):
    print('猫')
    if request.method == "POST":
        print('犬')
        new_username = request.POST['username']
        new_password = request.POST['password']
        user = authenticate(request, username=new_username, password=new_password)
        if user is not None:
            print('ニャン')
            login(request, user)
            return redirect('talk:list')
        else:
            print('わん')
            messages.error(request, 'ログインに失敗しました')
    return render(request,'accounts/login.html') 

# class LoginView(generic.CreateView):
#     def post(self, request, *arg, **kwargs):
#         form = LogInForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             user = User.objects.get(username=username)
#             login(request, user)
#             return redirect('/')
#         return render(request, 'login.html', {'form': form,})

#     def get(self, request, *args, **kwargs):
#         form = LogInForm(request.POST)
#         return render(request, 'login.html', {'form': form,})

# account_login = LogInForm.as_view()

# class LoginView(generic.CreateView):
#     form_class = LogInForm
#     success_url = reverse_lazy('talk:list')
#     template_name = 'accounts/login.html'