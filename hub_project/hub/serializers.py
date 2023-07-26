from rest_framework import serializers
from .models import User, Accomodation, Student

class AccomodationSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(
        view_name = 'student_detail',
        read_only=True
    )

    class Meta:
        model = Accomodation
        fields = ('id', 'student_name', 'bullet_list')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(
        view_name = 'student_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'clearance')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    teachers = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        many=True,
        read_only=True
    )

    caseworker = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )

    accomodations = serializers.HyperlinkedRelatedField(
        view_name = 'accomodation_detail',
        read_only=True
    )

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'learning_plan', 'teachers', 'caseworker', 'accomodations', 'teacher_suggestions')