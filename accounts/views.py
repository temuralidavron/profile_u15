from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect

from accounts.forms import RegisterForm, LoginForm, UpdateProfileForm, ChangeRoleUser, UserAddGroupForm, \
    ForgetPasswordForm, DonePasswordForm
from .models import Profile, CustomUser, Code
from .utils import send_html_email


# from .permissions import extra_admin


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



# @extra_admin
def change_role_user(request):
    if request.method=='POST':
        form=ChangeRoleUser(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('user')
            role=form.cleaned_data.get('role')
            user.role=role
            user.save()
            return redirect('list')
    else:
        form=ChangeRoleUser()
    return render(request,'accounts/change.html',{'form':form})

@login_required
def user_add_group(request):
    if request.method=='POST':
        form=UserAddGroupForm(request.POST)
        if form.is_valid():

            user=form.cleaned_data.get('user')
            print(user,type(user))
            group=form.cleaned_data.get('group')
            # customuser=CustomUser.objects.get(user=user)
            # groups=Group.objects.get(group=group)
            # if customuser is not None and groups is not None:
            # group.add(user)
            user.groups.add(group)
            return redirect('list')
    else:
        form=UserAddGroupForm()
    return render(request,'accounts/change.html',{'form':form})



def forget_password(request):
    if request.method=='POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            user=CustomUser.objects.filter(username=username,email=email).first()
            if user:
                code=Code.objects.create(user=user)
                send_html_email(code.code,user.email,user.username)
                return redirect('send')
            else:
                redirect('login')

    else:
        form=ForgetPasswordForm()
    return render(request,"accounts/forget.html",{'form':form})



def done_password(request):
    name=request.GET.get('name')
    form=DonePasswordForm()
    return render(request,"accounts/done.html",{'form':form})

