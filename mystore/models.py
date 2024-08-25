from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICES=(
    ('cr','crud'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Panner'),
    ('GH','Ghee'),
    ('CZ','cheese'),
    ('IC','Ice-Cream'),
)
STATE_CHOICES=(
    ("JK","jamu&kashmir"),
    ("HM","Himachal Pradesh"),
    ("CH","Chandighar"),
    ("HR","Haryana"),
    ("UP","Utar Pradesh"),
    ("BH","Bihar"),
    ("WB","West Bangal"),
    ("OS","Odisha"),
    ("KR","Kerela"),
    ("TM","Tamil Nadu"),
    ("AM","assam"),
    ("TR","Tripura"),
    ("NL","Nagaland"),
    ("HM","Himaliya"),
    ("MN","Manipur"),
    ("SK","Skkim"),
    ("LH","Leh"),
    ("LD","ladahk"),
    ("AB","Andman Nicobar"),
    ("GA","Goa"),
    ("MP","Madhiya Pradesh"),
    ("MH","Maharastra"),
    ("UT","Utrakhand"),
    
    
)
# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discription=models.TextField()
    composition=models.TextField(default="")
    prodapp=models.TextField(default="")
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price
    
    
    

