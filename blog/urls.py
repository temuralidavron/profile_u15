from django.urls import path
from blog import views

urlpatterns=[
    path('',views.get_blog,name='list'),
    path('create/blog/',views.create_blog,name='create-blog'),
    path('update/blog/<int:pk>/',views.update_blog,name='update-blog'),
    path('detail/blog/<int:pk>/',views.detail_blog,name='detail-blog'),
    path('delete/blog/<int:pk>/',views.delete_blog,name='delete-blog'),
]