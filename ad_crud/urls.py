from django.urls import path, include
from .api_views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(
        "offers",
        OfferList.as_view(),
        name="list-offer",
    ),
    path(
        "offers/<int:pk>",
        OfferView.as_view(),
        name="view-offer",
    ),
    path(
        "category",
        CategoryList.as_view(),
        name="list-category",
    ),
    path(
        "category/<int:pk>",
        CategoryView.as_view(),
        name="view-category",
    ),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)