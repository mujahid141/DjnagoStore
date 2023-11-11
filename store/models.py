from django.db import models
class Promotions(models.Model):
    description = models.CharField(max_length=225)
    discount = models.FloatField()

class Collection(models.Model):
    Name = models.CharField(max_length=225)
    dscription = models.TextField()
    


class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    inventry = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,primary_key=True )
    promotions = models.ManyToManyField(Promotions)

class Customer(models.Model):
    MEMBERSHIP_B = 'B'
    MEMBERSHIP_S = 'S'
    MEMBERSHIP_G = 'G'
    
    MEMBERSHIP_CHIOCES =[
        (MEMBERSHIP_B,'Bronz'),
        (MEMBERSHIP_B,'Silver'),
        (MEMBERSHIP_B,'Gold'),
    ]
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHIOCES, default=MEMBERSHIP_B)
    
class Order(models.Model):
    PAYMENT_P ='P'
    PAYMENT_C ='C'
    PAYMENT_F ='F'
    PAYMENT_CHOICES =[
        (PAYMENT_P,'Pneding'),
        (PAYMENT_C,'Complete'),
        (PAYMENT_F,'Failed'),
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_CHOICES,default=PAYMENT_P)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,primary_key=True)
    
class Addres(models.Model):
    Street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    zip = models.IntegerField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,primary_key=True )




class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order , on_delete=models.CASCADE,primary_key=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=3)
    
    
class Cart(models.Model):
    craeted_at = models.DateField(auto_now_add=True)

class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField()
  