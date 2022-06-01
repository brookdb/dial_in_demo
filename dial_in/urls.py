
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  #admin page
    path('roast/', include('apps.roast.urls')), #roast app
    path('brew/', include('apps.brew.urls')), #roast app
    #path('about/', views.about, name="about"), #about page
    path('', views.landing, name="landing"), #landing page
    #path('accounts/', include('accounts.urls'))
    path('users/', include('apps.users.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
