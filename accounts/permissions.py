from django.shortcuts import redirect

def login_user(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request,*args,**kwargs)


    return wrapper