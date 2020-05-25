from rest_framework import serializers
from ..models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id',
                  'name',
                  'surname',
                  'birth_date',
                  'email_address',
                  'mobile_number',
                  'weight',
                  'wetsuit_size',
                  'harness_size',
                  'stay_location',
                  'iko_id',
                  'iko_level',
                  'arrival_date',
                  'leave_date',
                  'comment',
                  'register_date',

                  ]
        read_only_fields = ['id']