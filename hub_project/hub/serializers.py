from rest_framework import serializers
from .models import User, Accomodation, Student

class AccomodationSerializer(serializers.HyperlinkedModelSerializer):
    # student = serializers.HyperlinkedRelatedField(
    #     view_name = 'student_detail',
    #     read_only=True
    # )

    # student_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Student.objects.all(),
    #     source='first_name'
    # )

    class Meta:
        model = Accomodation
        fields = ('id', 'student_name', 'bullet_list')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # student = serializers.HyperlinkedRelatedField(
    #     view_name = 'student_detail',
    #     many=True,
    #     read_only=True
    # )

    # teacher_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='first_name'
    # )

    # caseworker_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='first_name'
    # )

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

    # teachers_2 = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='email'
    # )

    # caseworker = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     source='first_name'
    # )

#     teacher_url = serializers.ModelSerializer.serializer_url_field(
#         view_name='user_detail'
#    )
    
#     caseworker_url = serializers.ModelSerializer.serializer_url_field(
#         view_name='user_detail'
#    )

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'learning_plan', 'teachers', 'caseworker', 'accomodations', 'teacher_suggestions')