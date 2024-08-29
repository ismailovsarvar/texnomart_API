import json
import os

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from texnomart.models import Category, Group, Product

""" Category va Productga yangi ma'lumotlar qo'shganda email orqali signal jo'natish """


def send_creation_email(subject, message):  # Yuborish uchun umumiy funksiyani yaratamiz.
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # settings.py faylida default email sozlangan
        [settings.NOTIFICATION_EMAIL],  # Yuboruvchi email
        fail_silently=False,
    )


@receiver(post_save, sender=Category)
def send_category_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Category Created'
        message = f'A new category has been created:\n\nTitle: {instance.title}'
        send_creation_email(subject, message)


@receiver(post_save, sender=Group)
def send_group_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Group Created'
        message = f'A new group has been created:\n\nTitle: {instance.title}\nCategory: {instance.category.title}'
        send_creation_email(subject, message)


@receiver(post_save, sender=Product)
def send_product_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Product Created'
        message = f'A new product has been created:\n\nName: {instance.name}\nDescription: {instance.description}\nPrice: {instance.price}\nDiscount: {instance.discount}\nGroup: {instance.group.title}'
        send_creation_email(subject, message)


""" Category va Product ma'lumotlari o'chirilganda json faylga saqlash """

# Saqlanadigan papka yo'li
DIRECTORY_PATH = 'texnomart/deleted'

# Fayllar uchun yo'llar
CATEGORIES_FILE_PATH = os.path.join(DIRECTORY_PATH, 'categories.json')
PRODUCTS_FILE_PATH = os.path.join(DIRECTORY_PATH, 'products.json')

# Papka mavjudligini tekshirish yoki yaratish
if not os.path.exists(DIRECTORY_PATH):
    os.makedirs(DIRECTORY_PATH)


def save_deleted_data(file_path, data):
    # Eski ma'lumotlarni o'qish
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Yangi ma'lumotlarni qo'shish
    existing_data.append(data)

    # Ma'lumotlarni JSON faylga yozish
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)


@receiver(pre_delete, sender=Category)
def save_category_before_delete(sender, instance, **kwargs):
    # O'chirilayotgan kategoriya ma'lumotlarini JSON formatida saqlash
    data = {
        'model': 'Category',
        'id': instance.id,
        'title': instance.title,
        'slug': instance.slug,
        'image': instance.image.url if instance.image else None,  # URL formatida saqlash
    }
    save_deleted_data(CATEGORIES_FILE_PATH, data)


@receiver(pre_delete, sender=Product)
def save_product_before_delete(sender, instance, **kwargs):
    # Product modelida ManyToManyField mavjud bo'lgani uchun 'like'larni userlarga bog'lab olamiz
    likes = list(instance.is_liked.values_list('id', flat=True))

    # O'chirilayotgan product ma'lumotlarini JSON formatida saqlash
    data = {
        'model': 'Product',
        'id': instance.id,
        'name': instance.name,
        'slug': instance.slug,
        'description': instance.description,
        'price': instance.price,
        'discount': instance.discount,
        'group': instance.group.id if instance.group else None,
        'is_liked': likes
    }
    save_deleted_data(PRODUCTS_FILE_PATH, data)
