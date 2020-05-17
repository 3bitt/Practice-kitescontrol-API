from django.db import models
from django.db.models import DO_NOTHING

from .instructor import Instructor


class InstructorHoursByDate(models.Model):
    class Meta:
        managed = False
        db_table = 'VW_INSTRUCTOR_HOURS'

    instructor_id = models.ForeignKey(Instructor, on_delete=DO_NOTHING, related_name='instructor')
    name = models.CharField()
    surname = models.CharField()
    date = models.DateField()
    single_hours = models.FloatField()
    group_hours = models.FloatField()
    pay_rate = models.IntegerField()
