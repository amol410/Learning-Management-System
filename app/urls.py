
from app import views
from django.urls import path

urlpatterns = [
    path('base', views.BASE, name='base'),
    path('404', views.PAGE_NOT_FOUND, name='404'),
    path('', views.HOME, name='home' ),
    path('courses', views.SINGLE_COURSE, name='single_course'),
    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),
    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),
    path('courses/filter-data',views.filter_data,name="filter-data"),
    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my_course', views.MY_COURSE, name='my_course'),
    path('verify_payment', views.VERIFY_PAYMENT, name='verify_payment'),
]

