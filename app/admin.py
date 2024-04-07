from django.contrib import admin

# Register your models here.
from .models import *

class what_you_learn_TubularInline(admin.TabularInline):
    model = What_you_learn

class requirements_TubularInline(admin.TabularInline):
    model = requirements     

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TubularInline, requirements_TubularInline)


admin.site.register(Categories)
admin.site.register(Course, course_admin)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(What_you_learn)
admin.site.register(requirements)