from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from dataclasses import fields
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('uuid', 'name', 'module', 'price',)


class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ('uuid', 'first_name', 'last_name', 'author', 'degree', 'subject',)


class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ('uuid', 'first_name', 'last_name', 'group', 'author', 'email', 'phone', 'course', 'subjects',)
        
        def validate(self, value):
            if value['course']>5:
                raise serializers.ValidationError("Course is too big")
            return value


        