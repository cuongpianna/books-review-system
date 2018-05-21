from _threading_local import local

from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q

# Create your views here.
from .models import Book,Comment,Status,Rate
from .forms import CommentForm
from actions.utils import create_action
from booksystem.common.decorators import ajax_login_required

def index(request):
    books = Book.objects.all()
    status = Status.objects.all()
    return render(request,'books/index.html',{'books':books,'status':status,'range':(1,6)})

def detail(request,slug):
    book = Book.objects.get(slug=slug)
    comments = book.comments.order_by('-timestamp').filter(parent__isnull=True)[:6]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #text = form.get
            parrent_obj = None
            try:
                parrent_id = int(request.POST.get('parrent_id'))
            except:
                parrent_id = None

            if parrent_id:
                parrent_obj = Comment.objects.get(id = parrent_id)
                if parrent_obj:
                    repply_cmt = Comment(user=request.user, book=book, text=form.cleaned_data['text'])
                    repply_cmt.parrent = parrent_obj
            new_comment = form.save(commit=False)
            new_comment.book = book
            new_comment.user =request.user
            new_comment.save()

            # cmt = Comment(book=book,user=request.user,text=form.cleaned_data["text"])
            # cmt.save()
    else:
        form = CommentForm()

    return render(request, 'books/detail.html', {'book': book,'cmts':comments,'form':form})

def read_book(request,slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/read.html', {'book': book})

@require_POST
@csrf_exempt
def update_status(request):
    if request.user.is_authenticated:
        ss = request.POST.get('status')
        book_id = request.POST.get('book_id')
        try:
            b = Book.objects.get(id=book_id)
            try:
                old_status = Status.objects.get(user=request.user, book=b)
            except:
                old_status = None
            if old_status is not None:
                if ss == "1":
                    old_status.status = "1"
                    old_status.save()
                    create_action(request.user, 'đánh dấu sách', b)
                elif ss == "2":
                    old_status.status = "2"
                    old_status.save()
                    create_action(request.user, 'đánh dấu sách', b)

                else:
                    old_status.status = "3"
                    old_status.save()
                    create_action(request.user, 'đánh dấu sách', b)


                if old_status.status == "1":
                    tt = "Chưa đọc"
                elif old_status.status == "2":
                    tt = "Đang đọc"
                else:
                    tt = "Đã đọc"
            else:
                new_status = Status(user=request.user,book=b)
                new_status.save()
                if ss == "1":
                    new_status.status = "1"
                    new_status.save()
                    create_action(request.user, 'đánh dấu sách', b)
                elif ss == "2":
                    new_status.status = "2"
                    new_status.save()
                    create_action(request.user, 'đánh dấu sách', b)
                else:
                    new_status.status = "3"
                    new_status.save()
                    create_action(request.user, 'đánh dấu sách', b)
                if new_status.status == "1":
                    tt = "Chưa đọc"
                elif new_status.status == "2":
                    tt = "Đang đọc"
                else:
                    tt = "Đã đọc"

            return JsonResponse({'text': tt})
        except:
            b = None
            return JsonResponse({'status': 'ko', 'b': book_id})
        return JsonResponse({'status': ss, 'au': True})
    return JsonResponse({'not_au':"1"})

@require_POST
@csrf_exempt
def update_rate(request,id):
    status = request.POST.get('status')
    book_id = request.POST.get('book_id')

    star = request.POST.get('star')
    try:
        book = Book.objects.get(id=book_id)
        try:
            old_rate = Rate.objects.get(user=request.user, book=book)
        except:
            old_rate = None

        if old_rate is not None:
            old_rate.rate = star
            old_rate.save()
            create_action(request.user, 'đánh giá sách', book)
            return JsonResponse({'save':'ok'})
        else:
            new_rate = Rate(user=request.user, book=book, rate=star)
            new_rate.save()
            create_action(request.user, 'đánh giá sách', book)
            return JsonResponse({'save': 'ko',})
    except:
        book = None
    return JsonResponse({'status': 's'})

def search(request):
    query = request.GET.get('q')

    results = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(title__icontains=query))

    return render(request,'books/search.html',{'results':results})



