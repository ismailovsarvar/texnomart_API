from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


""" Category modeli """


class Category(BaseModel):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='images/category/', null=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


"""END"""

""" Group modeli """


class Group(BaseModel):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='images/group/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='groups')

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


"""END"""

""" Product modeli """


class Product(BaseModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='products')
    is_liked = models.ManyToManyField(User, related_name='liked_products', blank=True)

    objects = models.Manager()

    @property
    def discounted_price(self) -> Any:
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100.0))
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


"""END"""

""" 'Product'ga bog'langan 'image' modeli """


class Image(BaseModel):
    image = models.ImageField(upload_to='images/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


"""END"""

""" Comment modeli"""


class Comment(BaseModel):
    class Rating(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    message = models.TextField()
    rating = models.IntegerField(choices=Rating.choices, default=Rating.One.value)
    file = models.FileField(null=True, blank=True, upload_to='comments/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


"""END"""

""" 'Product'ni attributlari """


class Key(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Value(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return self.product.name


"""END"""
