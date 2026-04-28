from django.shortcuts import render,redirect

from accounts.permissions import login_user
from .models import Blog
from .forms import BlogForm
# Create your views here.
def get_blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog/list.html',{'blogs':blogs})

@login_user
def create_blog(request):
    # user=request.user
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect("list")
        # if form.is_valid():
        #     form.owner = request.user.id
        #     form.save()
        #     # blog.owner=user.id
        #     return redirect("list")
    else:
        form=BlogForm()
    return render(request,"blog/create.html",{'form':form})