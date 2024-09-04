from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
            model = CustomUser
            fields = ['id','email', 'password', 'role', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
            extra_kwargs = {
                'password': {'write_only': True}, 
            }

    def create(self, validated_data):
        password = validated_data.pop('password', None)  
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password) 
        instance.save()
        return instance

    def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            return instance