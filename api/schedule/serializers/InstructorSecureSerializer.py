from rest_framework import serializers

from api.models import Schedule
from api.models import Instructor


class InstructorSecureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        exclude = ['birth_date',
                   'mobile_number',
                   'weight',
                   'available_from',
                   'available_to',
                   'pay_rate',
                   'english_lessons',
                   'kids_lessons',
                   'group_lessons',
                   'daily_hour_limit',
                   'active']
