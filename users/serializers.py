from django.contrib.auth import authenticate
from rest_framework import serializers

from user_type.serializer import UserTypeSerializer

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer de clase para serializar el modelo CustomUser.

    Este serializer se utiliza para convertir instancias del modelo CustomUser en
    representaciones JSON y viceversa. Define los campos a incluir en la serialización.

    Atributos:
    - Meta: Define el modelo y los campos a incluir en la serialización.

    """
    class Meta:
        model = CustomUser
        fields = ("id", "username", 'name', 'last_name', "email", "type_user")


class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer de clase para serializar las solicitudes de registro y crear un nuevo usuario.

    Este serializer se utiliza para convertir solicitudes de registro en instancias
    del modelo CustomUser y crear nuevos usuarios. Define los campos requeridos para
    el registro y oculta la contraseña en la respuesta.

    Atributos:
    - Meta: Define el modelo, los campos requeridos y los campos de escritura en la serialización.

    Métodos:
    - create: Crea un nuevo usuario utilizando los datos validados.

    """

    class Meta:
        model = CustomUser
        fields = ("id", "dni", "username", "name",
                  "last_name", "email", "password", "type_user")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)  # type:ignore


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer de clase para autenticar usuarios con DNI y contraseña.

    Este serializer se utiliza para validar las credenciales de inicio de sesión
    de los usuarios utilizando su DNI y contraseña. Si las credenciales son válidas,
    devuelve el usuario autenticado.

    Atributos:
    - dni: Campo para ingresar el número de DNI del usuario.
    - password: Campo para ingresar la contraseña del usuario.
    - type_user: Serializer para el tipo de usuario del usuario autenticado.

    Métodos:
    - validate: Valida las credenciales del usuario y devuelve el usuario autenticado
      si las credenciales son correctas.

    """

    dni = serializers.CharField()
    password = serializers.CharField(write_only=True)
    type_user = UserTypeSerializer(
        source='customuser.type_user', read_only=True)

    def validate(self, data):

        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
