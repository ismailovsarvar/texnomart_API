from django.urls import path
from texnomart.views import category, group, product, auth
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    # Category URL
    path('category/', category.CategoryApiView.as_view(), name='category-list'),
    path('add-category/', category.CategoryApiView.as_view(), name='add-category'),
    path('category/<slug:slug>/delete/', category.CategoryDetailApiView.as_view(), name='category-delete'),
    path('category/<slug:slug>/edit/', category.CategoryDetailApiView.as_view(), name='category-edit'),

    # Group URL
    path('category/<slug:slug>/', group.GroupCreateApiView.as_view(), name='group-list'),
    path('group/', group.GroupListApiView.as_view(), name='group-list'),
    path('group/<slug:slug>/detail/', group.GroupDetailApiView.as_view(), name='group-detail'),

    # Product URL
    path('product/', product.ProductCreateApiView.as_view(), name='product-list'),

        # Slug orqali qidirish uchun
    path('product/detail/slug/<slug:slug>/', product.ProductDetailApiView.as_view(), name='product-detail-slug'),

        # ID orqali qidirish uchun
    path('product/detail/<int:id>/', product.ProductDetailApiView.as_view(), name='product-detail-id'),

        # Slug orqali edit va delete qilish uchun
    path('product/slug/<slug:slug>/edit/', product.ProductDetailApiView.as_view(), name='product-edit-slug'),
    path('product/slug/<slug:slug>/delete/', product.ProductDetailApiView.as_view(), name='product-delete-slug'),

        # ID orqali edit va delete qilish uchun
    path('product/<int:id>/edit/', product.ProductDetailApiView.as_view(), name='product-edit-id'),
    path('product/<int:id>/delete/', product.ProductDetailApiView.as_view(), name='product-delete-id'),

    # Product Attribute URL
    path('product-attribute/', product.ProductAttributeCreateApiView.as_view()),
    path('product-attribute/<slug:slug>/detail/', product.ProductAttributeDetailApiView.as_view()),
    path('attribute-key/', product.KeyApiView.as_view()),
    path('attribute-value/', product.ValueApiView.as_view()),

    # Login URL

    # Token URL
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
