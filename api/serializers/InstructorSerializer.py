from rest_framework import serializers
from ..models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    weight = serializers.FloatField(required=False, allow_null=True)
    available_from = serializers.DateField(required=False, allow_null=True)
    available_to = serializers.DateField(required=False, allow_null=True)
    iko_id = serializers.IntegerField(required=False, allow_null=True)
    daily_hour_limit = serializers.FloatField(required=False, allow_null=True)

    class Meta:
        model = Instructor
        fields = [
            'id',
            'name',
            'surname',
            'nickname',
            'mobile_number',
            'birth_date',
            'email_address',
            'weight',
            'available_from',
            'available_to',
            'iko_id',
            'iko_level',
            'pay_rate_single',
            'pay_rate_group',
            'english_lessons',
            'kids_lessons',
            'group_lessons',
            'daily_hour_limit',
            'active'
        ]
        read_only_fields = ['id']
