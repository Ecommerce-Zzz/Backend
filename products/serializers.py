from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    on_stack = serializers.SerializerMethodField(read_only=True)
    owner = serializers.CharField(source="owner.username", read_only=True)
    available = serializers.BooleanField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "owner",
            "available",
            "on_stack",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return super().create(validated_data)

    def save(self, *args, **kwargs):
        return super().save(**kwargs)

    def get_on_stack(self, obj):
        if obj.available:
            return "On stack"
        return "Out of stack"
