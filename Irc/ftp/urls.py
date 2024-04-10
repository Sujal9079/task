from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="index"),
    path('', views.index, name='index'),
    path('', views.index, name='network_expansion'),
    path('',views.index,name="cards"),
    path('', views.index, name='reviews'),
    path('games/', views.index, name='game_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
