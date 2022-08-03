from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import generics


#Teacher List
class CreateTeacherView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListTeacherView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class DestroyTeacherView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'uuid'


class UpdateTeacherView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'uuid'


#Student List
class CreateStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListStudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DestroyStudentView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'uuid'


class UpdateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'uuid'


#Subject List
class CreateSubjectView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListSubjectView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DestroySubjectView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'uuid'


class UpdateSubjectView(generics.UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'uuid'




