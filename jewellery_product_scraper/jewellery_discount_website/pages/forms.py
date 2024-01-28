from django.forms import FileField, Form, ModelForm
from .models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = [
            "title",
            "price",
            "original_price",
            "sale_discount",
            "stone_type",
            "metal_type",
        ]


class UploadForm(Form):
    products_file = FileField()
