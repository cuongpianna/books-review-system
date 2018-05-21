from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',auth_views.login,{'template_name':'users/login.html'},name='login'),
    path('logout',auth_views.logout,{'template_name':'users/logout.html',},name='logout'),
    path('logout-then-login',auth_views.logout_then_login,name='logout-then-login'),
    path('show/<username>',views.profile,name='profile'),
    path('review/list/<username>/<status>/',views.review_list,name='review-list'),


]