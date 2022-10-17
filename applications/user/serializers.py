from rest_framework import serializers
from .models import User, Role

# User Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'name',
        )
        
class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = User
        fields = ('id','username', 'role')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email','fullname','dni','password','role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'], email = validated_data['email'], fullname= validated_data['fullname'],
            dni= validated_data['dni'], password= validated_data['password'],role= validated_data['role'])
        return user


class CustomSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = User
        fields = (
            'id',
            'fullname',
            'username',
            'email',
            'dni',
            'role',
            'password'
        )

class ModifySerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('id','username', 'email','fullname','dni','password','role')
        extra_kwargs = {'password': {'write_only': True}}