from .models import Profile,Skill
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def paginatorHelper(request,profiles,result):
    page = request.GET.get('page')
    paginator = Paginator(profiles,result)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = max(1,int(page)-4)
    right_index = min(int(page)+5,paginator.num_pages+1)
    custom_range = range(left_index,right_index)

    return profiles,paginator,custom_range

def searchHelper(request):
    search_query = ''
    if request.GET.get('text'):
        search_query = request.GET.get('text')
    #print("Search = ",search_query)

    skill = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skill)
        )

    return profiles,search_query