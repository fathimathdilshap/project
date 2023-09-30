from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home),
    path('reg',views.reg),
    path('log',views.log),
    path('pro',views.pro),
    path('view',views.view),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)