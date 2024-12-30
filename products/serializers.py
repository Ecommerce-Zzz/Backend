from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    on_stack = serializers.SerializerMethodField(read_only=True)
    owner = serializers.CharField(source="owner.username", read_only=True)
    available = serializers.BooleanField(write_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product_detail", lookup_field="pk", read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "url",
            "title",
            "description",
            "price",
            "owner",
            "available",
            "on_stack",
        ]

    """
        Removing description field if the endpoint is product list otherwise, 
        the description field will show when posting new data or in product detail endpoint
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context["request"] or None
        if (
            request
            and request.method == "GET"
            and request.resolver_match.url_name == "product_list_create"
        ):
            self.fields.pop("description")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return super().create(validated_data)

    def get_on_stack(self, obj):
        if obj.available:
            return "On stack"
        return "Out of stack"
