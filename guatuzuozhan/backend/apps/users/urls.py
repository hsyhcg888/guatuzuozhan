from django.urls import path
from .views import AdminActionView, AdminUserDetailView, AdminUsersView, DepartmentListView, LoginView, MeView, RegisterView, UserImportView, UserTemplateView
urlpatterns = [
    path('auth/register/', RegisterView.as_view()), path('auth/login/', LoginView.as_view()), path('auth/me/', MeView.as_view()), path('auth/departments/', DepartmentListView.as_view()),
    path('admin/users/', AdminUsersView.as_view()), path('admin/users/template/', UserTemplateView.as_view()), path('admin/users/import/', UserImportView.as_view()), path('admin/users/<int:pk>/', AdminUserDetailView.as_view()), path('admin/users/<int:pk>/<str:action>/', AdminActionView.as_view()),
]
