from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from.views import home,about,contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home,name="home"),
    url(r'^about/',about,name="about"),
    url(r'^contact/',contact,name="contact"),
    url(r'^profiles/', include('accounts.urls', namespace='accounts')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^seller/', include('sellers.urls', namespace='sellers')),
    url(r'^accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
