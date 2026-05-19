from django.urls import path
from blog import views, blog_class_view

urlpatterns=[
    path('',views.get_blog,name='list'),
    path('create/blog/',views.create_blog,name='create-blog'),
    path('export/blog/',views.export_blogs_to_excel,name='export-blog'),
    path('update/blog/<int:pk>/',views.update_blog,name='update-blog'),
    path('like/blog/<int:post_id>/',views.like_post,name='like_post'),
    path('detail/blog/<int:pk>/',views.detail_blog,name='detail-blog'),
    path('delete/blog/<int:pk>/',views.delete_blog,name='delete-blog'),


    # url Class view
    path('list/class/',blog_class_view.BlogListView.as_view(),name='list-class'),
    path('class/<int:pk>/',blog_class_view.BlogDetailView.as_view(),name='detail-class'),
    path('class/create/',blog_class_view.BlogCreateView.as_view(),name='create-class'),
    path('class/update/<int:pk>/',blog_class_view.BlogUpdateView.as_view(),name='update-class'),
    path('class/delete/<int:pk>/',blog_class_view.BlogDeleteView.as_view(),name='delete-class'),
]