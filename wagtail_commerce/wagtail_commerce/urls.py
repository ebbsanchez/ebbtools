from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from .views import testing_page
from accounts.views import clear_books

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    path('products/clear', clear_books, name="clear"),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^shopping_cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    


    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),


    # Ecommerce Site Practice


]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
