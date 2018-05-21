from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('<int:id>/update-rate',views.update_rate,name='update-rate'),
    path('update', views.update_status, name='update'),
    path('<slug>/detail',views.detail,name = 'detail'),
    path('<slug>/read',views.read_book,name='read'),

]