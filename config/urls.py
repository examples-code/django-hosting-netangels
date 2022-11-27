from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from src.home.urls import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.home.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.STATIC_URL,
#         document_root=settings.STATIC_ROOT
#     )
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )


if settings.DEBUG:
    
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

handler404 = pageNotFound
