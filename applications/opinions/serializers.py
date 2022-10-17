from .models import OpinionsUser
from applications.user.serializers import UserSerializer
from rest_framework import serializers

class OpinionsUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpinionsUser
        fields = (
            'user',
            'comment',
            'attention',
            'place',
            'food',
            'price')


class ListUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = OpinionsUser
        fields = ('user','comment','created')