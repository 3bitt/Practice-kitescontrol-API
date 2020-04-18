from rest_framework import serializers

from api.models import Schedule
from api.models import Student


class StudentSecureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['arrival_date',
                   'leave_date',
                   'email_address',
                   'mobile_number',
                   'stay_location',
                   'register_date']
