import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User

# def randomQuerySet(items, size):
#     result = sorted(items, key=lambda x: random.random())
#     return result[:size]

def randomQuerySet(items, size): # сделать ModelManager для Tag и кинуть туда
    result = []
    ls = []
    if (size > items.count()):
        return items
    num = random.randrange(0, items.count())
    for i in range(size):
        while (num in ls):
            num = random.randrange(0, items.count())
        ls.append(num)
    for i in range(size):
        result.append(items[ls[i]])
    return result



def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    try:
        objects_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects_page = paginator.page(paginator.num_pages)
    return objects_page