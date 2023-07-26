# hub/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('accomodations/', views.AccomodationList.as_view(), name='accomodation_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('accomodations/<int:pk>', views.AccomodationDetail.as_view(), name='accomodation_detail')
]