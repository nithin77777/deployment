from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'email', 'mobile_no']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }
