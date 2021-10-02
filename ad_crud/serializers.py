from rest_framework import serializers
from .models import (
    Category,
    Offer
)


class CategorySerializerForList(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializerForOfferList(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ("id",)

class CategorySerializerCreateUpdate(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "ordering")

class OfferSerializerForList(serializers.ModelSerializer):
    category = CategorySerializerForOfferList()

    class Meta:
        model = Offer
        fields = ("id","title","price", "category")

class OfferSerializer(serializers.ModelSerializer):
    category = CategorySerializerForList()

    class Meta:
        model = Offer
        fields = "__all__"
        read_only_fields = ("id",)

class OfferSerializerCreateUpdate(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ("title", "description", "price","category")
