
from django.contrib import admin
from django.urls import path, include, re_path


from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EventWebSite.urls')),
    path('administrator/', include('Administrator.urls')),
    path('EventCommittee/', include('UserManager.urls')),
    path('eventHead/', include('EventHead.urls')),
    path('coordinator/', include('Coordinator.urls')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL+'media/favicon.ico')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += re_path(r'.+', never_cache(serve_static)),
