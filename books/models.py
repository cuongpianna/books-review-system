from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(max_length=255,blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField(blank=True,null=True)
    file = models.FileField(upload_to="book_storage/%Y/%m/%d")
    photo = models.ImageField(upload_to="image/%Y/%m/%d",blank=True)
    file = models.FileField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)

    def save(self,*arg,**kwargs):
        self.slug = slugify(self.title)
        super(Book,self).save(*arg,**kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null = True,blank=True, related_name='replies',on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('timestamp',)

class Status(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='status')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='status')
    timestamp = models.DateTimeField(auto_now_add=True)
    STATUS =(
        ('1','Chưa đọc'),
        ('2','Đang đọc'),
        ('3','Đã đọc'),
    )

    status = models.CharField(max_length=5,choices=STATUS)

    def __str__(self):
        status = ""
        if self.status=="1":
            status = "Chưa đọc"
        elif self.status == "2":
            status = "Đang đọc"
        else:
            status = "Đã đọc"
        return "{} {} {}".format(self.user.username,status,self.book.title)


class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rate')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='rates')
    timestamp = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return "{} được rate {} sao bởi {}".format(self.book.title,self.rate,self.user.username)





