from django.contrib import admin

# Register your models here.
from .models import *

class what_you_learn_TubularInline(admin.TabularInline):
    model = What_you_learn

class requirements_TubularInline(admin.TabularInline):
    model = requirements     

class Video_TubularInline(admin.TabularInline):
    model = Video     

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TubularInline, requirements_TubularInline, Video_TubularInline)

   


admin.site.register(Categories)
admin.site.register(Course, course_admin)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(What_you_learn)
admin.site.register(requirements)
admin.site.register(Lesson)
admin.site.register(Language)
admin.site.register(UserCourse)
admin.site.register(Payment)