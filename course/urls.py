from django.urls import path
from .views import *

urlpatterns = [
    path('subjectcreate/', CreateSubjectView.as_view(), name='create_subject'),
    path('subjectlist/', ListSubjectView.as_view(), name='list_subject'),
    path('subjectdelete/<uuid:uuid>/', DestroySubjectView.as_view(), name='delete_subject'),
    path('subjectupdate/<uuid:uuid>/', UpdateSubjectView.as_view(), name='update_subject'),

    path('teachercreate/', CreateTeacherView.as_view(), name='create_teacher'),
    path('teacherlist/', ListTeacherView.as_view(), name='list_teacher'),
    path('teacherdelete/<uuid:uuid>/', DestroyTeacherView.as_view(), name='delete_teacher'),
    path('teacherupdate/<uuid:uuid>/', UpdateTeacherView.as_view(), name='update_teacher'),

    path('studentcreate/', CreateStudentView.as_view(), name='create_student'),
    path('studentlist/', ListStudentView.as_view(), name='list_student'),
    path('studentdelete/<uuid:uuid>/', DestroyStudentView.as_view(), name='delete_student'),
    path('studentupdate/<uuid:uuid>/', UpdateStudentView.as_view(), name='update_student'),
    
]