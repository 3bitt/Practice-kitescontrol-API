from rest_framework import serializers
from ..models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'id',
            'name',
            'surname',
            'nickname',
            'mobile_number',
            'birth_date',
            'weight',
            'available_from',
            'available_to',
            'iko_level',
            'pay_rate',
            'english_lessons',
            'kids_lessons',
            'group_lessons',
            'daily_hour_limit',
            'active'
        ]
        read_only_fields = ['id']
