from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/lists.html'
    context_object_name='blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/details.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'

    # def get_object(self, pk=None):
    #     print('data',pk)

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

class BlogCreateView(CreateView):
    form_class = BlogForm
    template_name = 'blog/create_class.html'
    success_url = reverse_lazy('list-class')  #

    # def post(self, request, *args, **kwargs):
    #     self.object.owner = request.user
    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

        print(request)
        print(args)
        print(kwargs)




    # def get_object(self):
    #     blog=self.get_object()
    #     # blog.title.upper()
    #     return blog



# def detail_blog(request,pk):
#     blogs=Blog.objects.get(pk=pk)
#     return render(request,'blog/detail.html',{'blog':blogs})


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/update_class.html'
    success_url = reverse_lazy('list-class')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('list-class')

