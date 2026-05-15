from django.urls import path
from blog import views

urlpatterns=[
    path('',views.get_blog,name='list'),
    path('create/blog/',views.create_blog,name='create-blog'),
    path('export/blog/',views.export_blogs_to_excel,name='export-blog'),
    path('update/blog/<int:pk>/',views.update_blog,name='update-blog'),
    path('like/blog/<int:post_id>/',views.like_post,name='like_post'),
    path('detail/blog/<int:pk>/',views.detail_blog,name='detail-blog'),
    path('delete/blog/<int:pk>/',views.delete_blog,name='delete-blog'),
]