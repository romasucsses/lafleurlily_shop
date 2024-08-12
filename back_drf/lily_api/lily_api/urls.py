from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from lily_api import settings

urls_api_version_1 = [
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
]

urlpatterns = [
    path('api/admin/', admin.site.urls, name='admin_page'),
    path('api/v1/<str:db>/', include(urls_api_version_1)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
