from django.db import models

from users.models import User

class Page(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    context = models.TextField()
    page_keywords = models.TextField()
    page_description = models.TextField()

    def __str__(self):
        return self.slug

class Categories(models.Model):
    image = models.ImageField(upload_to="category_images")
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    page_keywords = models.TextField()
    page_description = models.TextField()

    def __str__(self):
        return self.slug


class ActionCatogory(models.Model):
    image = models.ImageField(upload_to="category_images")
    title = models.CharField(max_length=64)
    page_keywords = models.TextField()
    page_description = models.TextField()


class Subcategories(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="category_images")
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    page_keywords = models.TextField()
    page_description = models.TextField()

    def __str__(self):
        return self.slug

class Product(models.Model):
    subcategory = models.ForeignKey('Subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    page_keywords = models.TextField()
    page_description = models.TextField()
    size = models.CharField(max_length=255,blank=True)
    color = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    sale = models.BooleanField()
    prise_on_sale = models.FloatField()
    image = models.ImageField(upload_to="product_images")
    visible = models.BooleanField()
    time = models.DateTimeField()

    def __str__(self):
        return self.slug


class Comments(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} | {self.user}'

class Photos(models.Model):
    parent = models.ForeignKey("Product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.parent.title



class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.CharField(max_length=64,blank=True)
    color = models.CharField(max_length=64, blank=True)
    quantity = models.SmallIntegerField()
    in_progress = models.BooleanField(default=False)
    timer = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.user} add {self.product}'

    def sum(self):
        if self.product.sale:
            return self.product.prise_on_sale * self.quantity
        return self.product.price * self.quantity

class Order(models.Model):
    basket = models.ManyToOneRel(field=id,to=Basket,field_name=id)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    svaluedesteny = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    adress = models.CharField(max_length=255,blank=True)
    message = models.TextField(blank=True)
    total_sum = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'

class OrderBasket(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.CharField(max_length=64,blank=True)
    color = models.CharField(max_length=64, blank=True)
    quantity = models.SmallIntegerField()
    timer = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order} and {self.product}'
