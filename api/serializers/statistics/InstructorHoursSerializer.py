from rest_framework import serializers

from api.models.vw_instructorHours import InstructorHours


class InstructorHoursSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    # name = serializers.CharField()
    # surname = serializers.CharField()
    # date = serializers.DateField()
    # single_hours = serializers.FloatField()
    # group_hours = serializers.FloatField()
    # pay_rate = serializers.IntegerField()

    class Meta:
        model = InstructorHours
        fields = [
            'id',
            'name',
            'surname',
            'date',
            'single_hours',
            'group_hours',
            'pay_rate_single'
        ]