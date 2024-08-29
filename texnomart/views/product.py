from rest_framework import status, generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from texnomart import models, serializers, filters
from texnomart.models import Product

from texnomart.permissions import CustomPermission

"""PRODUCT GENERIC API VIEW"""


class ProductCreateApiView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductModelSerializer
    permission_classes = [IsAuthenticated]
    permission_classes_2 = [CustomPermission]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Product Successfully Created'}
        response.status_code = status.HTTP_201_CREATED
        return response


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    # Optimization
    # queryset = models.Product.objects.select_related('group', 'group__category').all()

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductModelSerializer
    permission_classes = [IsAuthenticated]
    permission_classes_2 = [CustomPermission]

    # lookup_field = 'slug'

    def get_object(self):
        if 'id' in self.kwargs:
            lookup_field = 'id'
            lookup_value = self.kwargs['id']
        elif 'slug' in self.kwargs:
            lookup_field = 'slug'
            lookup_value = self.kwargs['slug']
        else:
            raise NotFound({'message': 'Invalid lookup field.'})

        try:
            return self.queryset.get(**{lookup_field: lookup_value})
        except models.Product.DoesNotExist:
            raise NotFound({'message': f'Product not found with the provided {lookup_field}.'})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data = {'message': 'Product Successfully Updated'}
        response.status_code = status.HTTP_200_OK
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data = {'message': 'Product Successfully Deleted'}
        response.status_code = status.HTTP_200_OK
        return response


""" PRODUCT KEY AND VALUE VIEWS """


class KeyApiView(generics.ListCreateAPIView):
    queryset = models.Key.objects.all()
    serializer_class = serializers.KeyModelSerializer


class ValueApiView(generics.ListCreateAPIView):
    queryset = models.Value.objects.all()
    serializer_class = serializers.ValueModelSerializer


"""PRODUCT ATTRIBUTE API VIEW"""


class ProductAttributeCreateApiView(generics.ListCreateAPIView):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeModelSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Product Attribute Successfully Created'}
        response.status_code = status.HTTP_201_CREATED
        return response


class ProductAttributeDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Attribute.objects.all()
    serializer_class = serializers.AttributeModelSerializer
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data = {'message': 'Product Attribute Successfully Updated'}
        response.status_code = status.HTTP_200_OK
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data = {'message': 'Product Attribute Successfully Deleted'}
        response.status_code = status.HTTP_200_OK
        return response


"""FILTER""" # TEST SHAKLDA


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductModelSerializer
    filterset_class = filters.ProductFilter
    search_fields = ['name', 'description']
    filter_backends = (SearchFilter, DjangoFilterBackend)



""" PAGINATION """


class Pagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100
