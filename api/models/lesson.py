from django.db import models
from api.models import Student
from api.models import Instructor

class Lesson(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    student = models.ManyToManyField(Student, related_name='lessons')
    instructor = models.ManyToManyField(Instructor, related_name='lessons')
    duration = models.FloatField()
    in_progress = models.BooleanField(default=False, null=True, blank=True)
    paid = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    equipment = models.CharField(max_length=30, null=True, blank=True)
    kite_brand = models.CharField(max_length=30, null=True, blank=True)
    kite_size = models.FloatField(null=True, blank=True)
    board = models.CharField(max_length=30, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)

