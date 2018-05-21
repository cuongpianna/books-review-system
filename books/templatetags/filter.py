from django import template

from ..models import Status,Book

register = template.Library()

@register.filter
def get(book,user):
    try:
        s = book.status.get(user=user)
    except:
        s = None
    if s:
        if s.status == "1":
            tt = "Chưa đọc"
        elif s.status == "2":
            tt = "Đang đọc"
        else:
            tt = "Đã đọc"
    else:
        tt = "Chưa đọc"
    return tt

@register.filter
def ratefilter(book,user):
    try:
        b= book.rates.get(user=user)
        return b.rate
    except:
        b = None
        return 0