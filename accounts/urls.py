from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns=[
    path('register/',views.register_view,name='register'),
    path('send-email/',TemplateView.as_view(template_name='accounts/send.html'),name='send'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('forget/',views.forget_password,name='forget-password'),
    path('done/',views.done_password,name='done-password'),
    path('profile/',views.get_profile,name='profile'),
    path('update/',views.update_profile,name='update'),
    path('change/',views.change_role_user,name='change'),
    path('group/',views.user_add_group,name='add_group'),
]