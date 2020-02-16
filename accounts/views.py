from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    # def form_valid(self, form):
    #     print('いってっるよ')
    #     user = form.save() # formの情報を保存
    #     login(self.request, user) # 認証
    #     self.object = user 
    #     return HttpResponseRedirect(self.get_success_url()) #

    

def loginf(request):
    print('猫')
    if request.method == "POST":
        new_username = request.POST['username']
        new_password = request.POST['password']
        new_email = request.POST['email']
        user = authenticate(request, username=new_username, password=new_password, email=new_email)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('login')
    return render(request,'accounts/login.html') 
