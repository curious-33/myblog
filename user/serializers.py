from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('first_name','email','username','password')
        extra_kwargs = {'password': {'input_type':'password','write_only':True,'min_length': 8}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type":'password'})

    def validate(self,attrs):
        user = authenticate(**data)
        if user and user.is_active:
            attrs['user']=user
            return attrs
        msg = _("Unable to authenticate with provided credentials")
        return serializers.ValidationError(msg,code='authentication')  