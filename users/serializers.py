from django.core.validators import RegexValidator
from rest_framework import serializers

from avito import settings
from users.models import User, Location
from users.validators import EmailValidator


class UserAdSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "location"]


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name"
    )
    ads = serializers.IntegerField()

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    email = serializers.EmailField(max_length=50, validators=[EmailValidator(settings.DISABLED_EMAILS)])
    password = serializers.CharField(max_length=150, validators=[RegexValidator(
        '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_-])[\da-zA-Z!@#$%^&*()_-]{6,}$',
        message="Weak password."
                "Your password must contain at least 1 upper case, lower case, numeric, and special character."
                "Passwords must be at least 6 characters in length.")])

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)

        user.set_password(user.password)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for loc in self._location:
            loc_obj, _ = Location.objects.get_or_create(name=loc)
            user.location.add(loc_obj)

        user.save()
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
