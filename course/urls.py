from django.urls import path
from .views import *

urlpatterns = [
    path('subjectcreate/', CreateSubjectView.as_view(), name='create_subject'),
    path('subjectlist/', ListSubjectView.as_view(), name='list_subject'),
    path('subjectdelete/<uuid:uuid>/', DestroySubjectView.as_view(), name='delete_subject'),
    path('subjectupdate/<uuid:uuid>/', UpdateSubjectView.as_view(), name='update_subject'),
    
]