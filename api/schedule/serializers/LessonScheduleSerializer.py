from rest_framework import serializers

from api.models import Lesson
from api.schedule.serializers.InstructorSecureSerializer import InstructorSecureSerializer
from api.schedule.serializers.StudentSecureSerializer import StudentSecureSerializer


class LessonsScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['date','time','created_date',
                 'duration','paid','status','equipment',
                 'kite_brand','kite_size','board','comment',
                  'student','instructor']

    instructor = InstructorSecureSerializer(many=True)
    student = StudentSecureSerializer(many=True)


