from rest_framework import serializers, exceptions
from django.contrib.auth.models import User



class UserCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=68, min_length=3, write_only=True)
    password = serializers.CharField(max_length=68, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        user = User.objects.filter(username=attrs.get('username'))
        if user.exists():
            raise exceptions.ValidationError("Username already exists.")

        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise exceptions.ValidationError("The two passwords must be the same.")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )