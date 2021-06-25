from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.views import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()

router.register('department', DepartmentViewSet, basename='department')
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]