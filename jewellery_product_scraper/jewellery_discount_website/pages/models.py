from django.db import models

# Create your models here.
# class StoneType(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField()

#     class Meta:
#         ordering = ("name",)

#     def __str__(self):
#         return self.name


# class MetalType(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField()

#     class Meta:
#         ordering = ("name",)

#     def __str__(self):
#         return self.name


class Products(models.Model):
    # stone_type = models.ForeignKey(
    #     StoneType, related_name="products", on_delete=models.CASCADE
    # )
    # metal_type = models.ForeignKey(
    #     MetalType, related_name="products", on_delete=models.CASCADE
    # )
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=255)
    original_price = models.CharField(max_length=255)
    sale_discount = models.DecimalField(max_digits=6, decimal_places=2)
    stone_type = models.CharField(max_length=255)
    metal_type = models.CharField(max_length=255)

    def __str__(self):
        return self.title
