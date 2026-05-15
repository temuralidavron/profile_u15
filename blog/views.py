from django.contrib.auth.decorators import permission_required, login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from openpyxl import Workbook

# from accounts.utils import send_simple_email
from accounts.permissions import login_user, admin_permission
from .models import Blog
from .forms import BlogForm
# Create your views here.
def get_blog(request):
    search=request.GET.get('q',None)
    blogs=Blog.objects.all()
    if search:
        blogs=blogs.filter(Q(title__icontains=search) |
                           Q(description__icontains=search)
                           )
    paginator=Paginator(blogs,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)




    context={
        'blogs':page_obj,

    }



    return render(request,'blog/list.html',context)

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




#excel
def export_blogs_to_excel(request):
    # Yangi Excel workbook yaratamiz
    wb = Workbook()
    ws = wb.active
    ws.title = "Blogs"

    # Sarlavhalar
    ws.append(["ID", "title", "desc", "owner", "Created at"])

    # Ma’lumotlarni yozish
    for p in Blog.objects.all():
        ws.append([p.id, p.title, p.description, p.owner.username, p.created_at.strftime("%Y-%m-%d %H:%M")])

    # Javob sifatida Excel faylni yuboramiz
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'
    wb.save(response)
    return response



@login_required
def like_post(request, post_id):
   blog = get_object_or_404(Blog, id=post_id)

   if request.method == "POST":
       if request.user in blog.likes.all():
           # agar oldin like bosgan bo'lsa, like olib tashlanadi
           blog.likes.remove(request.user)
       else:
           # agar like bosmagan bo'lsa, like qo'shiladi
           blog.likes.add(request.user)

   return redirect('list')
