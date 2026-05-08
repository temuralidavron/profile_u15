from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,redirect
# from accounts.utils import send_simple_email
from accounts.permissions import login_user, admin_permission
from .models import Blog
from .forms import BlogForm
# Create your views here.
def get_blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog/list.html',{'blogs':blogs})

# @login_user
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




def update_blog(request,pk):
    blog=Blog.objects.get(pk=pk)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            if blog.owner != request.user:
                return redirect("list")
            blog.title=form.cleaned_data.get('title',blog.title)
            blog.description=form.cleaned_data.get('description',blog.description)
            blog.image=form.cleaned_data.get('image',blog.image)
            blog.save()
            return redirect("list")
    else:
        form=BlogForm(instance=blog)
    return render(request,"blog/create.html",{'form':form})




def detail_blog(request,pk):
    # send_simple_email()
    blogs=Blog.objects.get(pk=pk)
    return render(request,'blog/detail.html',{'blog':blogs})

# @admin_permission
@permission_required('blog.delete_post', login_url='list')
def delete_blog(request,pk):
    blog=Blog.objects.get(pk=pk)

    if request.method=='POST':
        blog.delete()
        return redirect('list')
    else:
        return render(request,'blog/delete.html',{'blog':blog})
