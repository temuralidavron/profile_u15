from django.shortcuts import redirect
from .models import UserRole

def login_user(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request,*args,**kwargs)


    return wrapper




def admin_permission(func):
    def wrapper(request,*args,**kwargs):
        # print(request.user)
        # print(request.user.role)
        if request.user.is_authenticated:
            if not request.user.role==UserRole.ADMIN:
                return redirect('list')
        return func(request,*args,**kwargs)
    return wrapper



def admin_or_manager_permission():
    pass



def extra_admin(func):
    def wrapper(request, *args, **kwargs):


        if request.user.is_authenticated:
            print(request.user.username)
            if not request.user.role == UserRole.ADMIN and not request.user.username=='tester99':
                return redirect('list')
        return func(request, *args, **kwargs)

    return wrapper