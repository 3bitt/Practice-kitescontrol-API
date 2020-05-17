from django.db import models
from django.db.models import DO_NOTHING

from .instructor import Instructor


class InstructorHours(models.Model):
    class Meta:
        managed = False
        db_table = 'vw_instructor_hours'

    # instructor_id = models.ForeignKey(Instructor, on_delete=DO_NOTHING, related_name='instructor')
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30 )
    surname = models.CharField(max_length=30)
    date = models.DateField()
    single_hours = models.FloatField()
    group_hours = models.FloatField()
    pay_rate = models.IntegerField()
