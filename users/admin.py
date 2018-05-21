from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','dirth_of_birth','sex','photo']

admin.site.register(Profile)

