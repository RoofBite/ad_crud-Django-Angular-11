from django.shortcuts import get_object_or_404, render
from rest_framework import generics, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .models import Category, Offer
from .serializers import (
    OfferSerializerForList,
    OfferSerializer,
    CategorySerializerForList,
    OfferSerializerCreateUpdate,
    CategorySerializer,
    CategorySerializerCreateUpdate
)


class CategoryList(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all().order_by("ordering")
    serializer_class = CategorySerializerForList
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def get_serializer_class(self):
        if self.request.method in ("POST",):
            return CategorySerializerCreateUpdate
        return CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OfferList(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializerForList
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = ("category",)

    def get_serializer_class(self):
        if self.request.method in ("POST",):
            return OfferSerializerCreateUpdate
        return OfferSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OfferView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OfferSerializer

    def get_object(self):
        pk = self.kwargs["pk"]
        return Offer.objects.get(pk=pk)

    def get_serializer_class(self):
        if self.request.method in ("PUT",):
            return OfferSerializerCreateUpdate
        return OfferSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CategorySerializer

    def get_object(self):
        pk = self.kwargs["pk"]
        return Category.objects.get(pk=pk)

    def get_serializer_class(self):
        if self.request.method in ("PUT",):
            return CategorySerializerCreateUpdate
        return CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
