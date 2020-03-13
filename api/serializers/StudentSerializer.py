from rest_framework import serializers
from ..models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','surname','birth_date','weight','register_date']
        read_only_fields = ['id']