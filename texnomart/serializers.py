from django.db.models import Avg
from rest_framework import serializers

from texnomart.models import (
    Category,
    Group,
    Product,
    Key,
    Value,
    Attribute
)


class CategoryModelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    group_count = serializers.SerializerMethodField()

    def get_group_count(self, instance):
        return instance.groups.count()

    class Meta:
        model = Category
        fields = '__all__'


class GroupModelSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only=True)
    category_slug = serializers.SlugField(source='category.slug', read_only=True)
    image = serializers.SerializerMethodField(method_name='foo')
    product_count = serializers.SerializerMethodField()

    def get_product_count(self, instance):
        return instance.products.count()

    def foo(self, obj):
        if obj.image:
            image_url = obj.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url) if request else image_url
        return None

    class Meta:
        model = Group
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    is_liked = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    all_images = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    comment_info = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_attributes(self, instance):
        attrs = instance.attributes.all().values('key__name', 'value__name')
        combined_attrs = {
            attr['key__name']: attr['value__name']
            for attr in attrs
        }
        return combined_attrs


    def get_all_images(self, instance):
        request = self.context.get('request', None)
        if not request:
            return []   # Kontekstda so‘rov mavjud bo‘lmaganda, zaxira variant
        images = instance.images.all().order_by('-is_primary', '-id')
        return [request.build_absolute_uri(image.image.url) for image in images]


    def get_avg_rating(self, product):
        avg_rating = product.comments.all().aggregate(avg=Avg('rating'))
        return avg_rating.get('avg')

    def get_images(self, obj):
        # image = Image.objects.filter(is_primary=True, product=obj).first()
        image = obj.images.filter(is_primary=True).first()
        if image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(image.image.url)
        return None

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            # if user in obj.is_liked.filter(id=user.id).exists():
            return obj.is_liked.filter(id=user.id).exists()
        return False

    def get_comment_info(self, obj):
        return obj.comments.all().values('message', 'rating', 'user__username')

    class Meta:
        model = Product
        fields = '__all__'


class KeyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = '__all__'


class ValueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


class AttributeModelSerializer(serializers.ModelSerializer):
    key = KeyModelSerializer(read_only=True)
    value = ValueModelSerializer(read_only=True)
    product = ProductModelSerializer(read_only=True)

    class Meta:
        model = Attribute
        fields = '__all__'