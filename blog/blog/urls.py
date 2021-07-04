from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# seo
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    path('', include('applications.users.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.entries.urls')),
    path('', include('applications.favorites.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns_main + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# objeto sitemap que genera un xml
sitemaps = {
    'site':Sitemap(
        [
            'app_home:index'
        ]
    ),
    'entries':EntrySitemap
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]


urlpatterns = urlpatterns_main + urlpatterns_sitemap