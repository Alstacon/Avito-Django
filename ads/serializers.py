from rest_framework import serializers

from ads.models import Ad
from users.serializers import UserAdSerializer


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    author = UserAdSerializer()

    class Meta:
        model = Ad
        fields = '__all__'
