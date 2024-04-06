
from app import views
from django.urls import path

urlpatterns = [
    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home' ),
    path('courses', views.SINGLE_COURSE, name='single_course'),
    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),
    path('product/filter-data',views.filter_data,name="filter-data"),
]

