from django.urls import path
from accounts import views

urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.get_profile,name='profile'),
    path('update/',views.update_profile,name='update'),
]