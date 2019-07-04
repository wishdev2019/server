

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from apps.user.models import Users



class UserSerializer(serializers.ModelSerializer):

    class Meta :
        model = Users
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Users.objects.all(),
                fields=('loginname',),
                message="用户名已存在!"
            ),
        ]

class UsersSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Users.objects.all(),
                fields=('loginname',),
                message="登录名重复！"
            ),
        ]