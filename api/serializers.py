from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    # в поле отобразится имя департамента
    department = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    # в поле отобразится фамилия и имя каждого из сотрудников департамента
    employees = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'employees']
