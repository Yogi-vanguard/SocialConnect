from .models import Project,Tag
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def paginatorHelper(request,projects,result):
    page = request.GET.get('page')
    paginator = Paginator(projects,result)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_index = max(1,int(page)-4)
    right_index = min(int(page)+5,paginator.num_pages+1)
    custom_range = range(left_index,right_index)

    return projects,paginator,custom_range

def searchHelper(request):
    search_query = ''
    if request.GET.get('text'):
        search_query = request.GET.get('text')
    
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags)
    )

    return projects,search_query