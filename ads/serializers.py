from rest_framework import serializers

from ads.models import Ad, Selection, Category
from users.models import User
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


class AdCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._cat = self.initial_data.pop("category", "")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)

        cat_obj, _ = Category.objects.get_or_create(name=self._cat)
        ad.category = cat_obj

        ad.save()
        return ad

    def validate_author(self, value):
        return self.context['request'].user


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        exclude = ["owner", "items"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )

    class Meta:
        model = Selection
        fields = '__all__'

    def validate_owner(self, value):
        return self.context['request'].user
