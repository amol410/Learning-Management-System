from django.contrib import admin
from django.urls import path, include
from .import views
from .import user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/register', user_login.REGISTER, name='register'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update' )
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
