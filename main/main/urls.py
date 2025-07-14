from django.contrib import admin
from django.urls import path,include
from . import views
from .views import upload_file
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    # path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    
    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
