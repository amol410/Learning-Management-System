from django.shortcuts import render, redirect
from app.models import Categories, Course, Level
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    
    context={'category' : category,
              'course'  : course
             
             }
    return render(request, 'main/home.html', context)

def SINGLE_COURSE(request):

    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    context={'category' : category,
             'level'    : level,
             'course'   : course,
             }
    return render(request, 'main/single_course.html', context)


def CONTACT_US(request):
    return render(request, 'main/contact_us.html')


def ABOUT_US(request):
    return render(request, 'main/about_us.html')


def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    
    
    if category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')

    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id') 
    else:
        course = Course.objects.all().order_by('-id')    
    
    context = {
        'course': course
    }
    t = render_to_string('ajax/course.html', context)
    return JsonResponse({'data': t})










