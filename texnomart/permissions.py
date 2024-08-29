from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Ochiq metodlar (SAFE_METHODS) uchun ruxsat berish
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST, PUT, PATCH, DELETE metodlari uchun faqat autentifikatsiyalangan foydalanuvchilar
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ['PATCH', 'PUT', 'DELETE']:
            return request.user.is_authenticated

        if request.method in 'POST':
            return request.user.is_authenticated
        return False