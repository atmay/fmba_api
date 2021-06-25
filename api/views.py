from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from .models import Employee, Department
from api.serializers import DepartmentSerializer, EmployeeSerializer

User = get_user_model()


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = []


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []
