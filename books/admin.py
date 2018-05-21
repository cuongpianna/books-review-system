from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Category,Comment,Status,Rate

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description','timestamp','release_date','photo','category','user',)
    list_filter = ('title','timestamp','release_date')
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('book','user','book',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('book','user','status','timestamp',)

class RateAdmin(admin.ModelAdmin):
    list_display = ('book','user','rate','timestamp')


admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Rate,RateAdmin)
