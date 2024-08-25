from django.contrib import admin
from.models import product,Customer,Cart
# Register your models here.
@admin.register(product)
class productadmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','selling_price','discription','product_image']


@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
    list_display=['id','name','locality','city','mobile','zipcode','state']

@admin.register(Cart)
class Cartadmin(admin.ModelAdmin):
    list_display=['user','product','quantity']