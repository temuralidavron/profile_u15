from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render,redirect

from accounts.forms import RegisterForm, LoginForm,UpdateProfileForm
from .models import Profile

# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            if user:
                Profile.objects.create(user=user)
                return redirect('list')
    else:
        form=RegisterForm()
    return render(request,"accounts/register.html",{'nurulloh':form})





def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            # user=User.objects.get(username=username,password=password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('list')
            else:
                redirect('login')
    form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')



# profile view

def get_profile(request):
    profile=Profile.objects.get(user=request.user)
    context={
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)


def update_profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method=="POST":
        form=UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile.avatar=form.cleaned_data.get('avatar',profile.avatar)
            profile.age=form.cleaned_data.get('age',profile.age)
            profile.bio=form.cleaned_data.get('bio',profile.bio)
            profile.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm(instance=profile)
    return render(request,'accounts/update.html',{'form':form})




