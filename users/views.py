from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Profile
from books.models import Book,Status,Rate,Comment
from .forms import UserRegister

def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            profile = Profile(user=new_user)
            profile.save()
            return HttpResponse("ok")
        else:
            return render(request,'users/register.html',{'form':form})
    else:
        form = UserRegister()
        return render(request, 'users/register.html', {'form': form})
    return render(request, 'users/register.html', {'form': form})

def profile(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request,'users/profile.html',{'user':user,'profile':profile})

def review_list(request,username,status):
    aa = 1
    if status == 'read':
        aa = 1
    if status == 'reading':
        aa = 2
    user = User.objects.get(username=username)
    list = Status.objects.filter(user=user, status=aa)
    return render(request,'users/list_review_book.html',{'list':list})
