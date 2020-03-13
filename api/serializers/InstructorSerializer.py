from rest_framework import serializers
from ..models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'surname', 'birth_date', 'weight']
        read_only_fields = ['id']
