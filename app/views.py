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
    return render(request, 'main/index.html', context)

def SINGLE_COURSE(request):

    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price=0).count
    PaidCourse_count = Course.objects.filter(price__gte=1).count



    context={'category' : category,
             'level'    : level,
             'course'   : course,
             'FreeCourse_count' : FreeCourse_count,
             'PaidCourse_count': PaidCourse_count,
             }
    return render(request, 'main/single_course.html', context)

    


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category
    }
    return render(request, 'main/contact_us.html', context)


def ABOUT_US(request):
    return render(request, 'main/about_us.html')


def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    print(price)
    
    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    
    elif price == ['PriceAll']:
        course = Course.objects.all()

    elif category:
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


def COURSE_DETAILS(request, slug):
    course = Course.objects.filter(slug = slug)
    category = Categories.get_all_category(Categories)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')    
    
    context = {
         'course':course,
         'category' : category

    }
    return render(request, 'course/course_details.html', context)

def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category
    }
    return render(request, 'error/404.html', context)











