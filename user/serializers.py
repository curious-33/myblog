from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': _("The two password fields didn't match.")})

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        user = get_user_model().objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'email', 'avatar', 'job', 'about', 'url', 'telegram', 'instagram',
            'twitter')
        extra_kwargs = {'avatar': {'read_only': True}}


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('avatar', )


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()

    old_password = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': _("The two password fields didn't match.")})
        validate_password(data['password'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return userionError(msg, code='authentication')
