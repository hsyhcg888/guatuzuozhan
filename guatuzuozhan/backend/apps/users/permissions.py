from rest_framework.permissions import BasePermission

class IsSystemAdmin(BasePermission):
    message = '只有系统管理员可以执行此操作'
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_active and user.is_system_admin)
