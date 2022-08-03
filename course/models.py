import email
from telnetlib import STATUS
from tokenize import group
from unicodedata import name
import uuid
from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=100, unique=True)
    module = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class Teacher(models.Model):
    STATUS_CHOICES = (
        ('MASTER','Master'), 
        ('SENIOR','Senior'),
        ('MIDDLE','Middle'),
        ('JUNIOR','Junior'),
        ('MAGISTR','Magistr'),
        ('PHD_CANDIDANT','PhD_Candidant'), 
        ('DOTSENT','Dotsent'),
        )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    author = models.ManyToManyField(User, related_name='teacher')
    degree = models.CharField(choices=STATUS_CHOICES, default='MASTER', max_length=15)
    subject = models.ManyToManyField(Subject, related_name='teacher')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'teacher'


class Student(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    group = models.PositiveIntegerField(null=True, blank=True)
    author = models.ManyToManyField(User, related_name='student')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    course = models.PositiveSmallIntegerField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='student')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'student'
    
    

