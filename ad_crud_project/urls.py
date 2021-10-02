from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ad_crud.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("ad_crud.urls")),
    path("", index, name='index'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)