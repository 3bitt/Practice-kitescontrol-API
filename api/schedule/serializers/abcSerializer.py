from django.db.models import Q
from rest_framework import serializers

from api.models import Instructor, Lesson
from .abcdeSerializer import abcdeSerializer



# class abcSerializer(serializers.Serializer):
#     instructors = serializers.SerializerMethodField('get_instr_lessons')
#
#     def get_instr_lessons(self, lesson):
#         instr = Instructor.objects.filter(lessons__in=lesson).distinct()
#         print('\nPRINT\n', instr)
#         serializer = CustomInstrSerializer(instr, many=True, context={'lessons':lesson})
#         return serializer.data

class abcSerializer(serializers.Serializer):
    instructors = serializers.SerializerMethodField('get_instr_lessons')

    def get_instr_lessons(self, lesson):
        # instr = Instructor.objects.filter(lessons__in=lesson).distinct()
        instr = Instructor.objects.filter(active=True)
        serializer = abcdeSerializer(instr, many=True, context={'lessons':lesson})
        return serializer.data

