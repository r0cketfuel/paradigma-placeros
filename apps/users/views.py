from apps.users                         import serializers
from django.contrib.auth                import get_user_model
from rest_framework                     import status, viewsets
from rest_framework.permissions         import AllowAny
from apps.user_type.permisions          import IsAdministrador, IsSuper
from rest_framework.response            import Response
from rest_framework_simplejwt.tokens    import RefreshToken
from django.contrib.auth.hashers        import make_password

User = get_user_model()

class UserRegisterationViewSet(viewsets.ModelViewSet):
    """
    Vista para el registro de nuevos usuarios.

    Esta vista permite a los clientes crear un nuevo usuario enviando una solicitud POST
    con los datos de registro. Los usuarios creados se guardan en la base de datos, y se les
    asigna un token de acceso y un token de actualización para la autenticación.

    Atributos:
    - queryset: Conjunto de usuarios, utilizado para consultar usuarios existentes.
    - serializer_class: Clase de serialización utilizada para validar y crear usuarios.
    - permission_classes: Permisos requeridos para acceder a esta vista (administradores o superusuarios).

    Métodos:
    - create: Crea un nuevo usuario utilizando los datos proporcionados en la solicitud POST.
    - update: Actualiza los datos de un usuario existente, incluida la contraseña si se proporciona.

    """
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterationSerializer
    permission_classes = [IsAdministrador | IsSuper]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(
            token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.POST.copy()
        if not data.get('password'):
            data['password'] = instance.password
        else:
            data['password'] = make_password(data['password'])
        serializer = self.get_serializer(
            instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginViewSet(viewsets.ModelViewSet):
    """
    Vista para la autenticación de usuarios existentes.

    Esta vista permite a los usuarios autenticarse utilizando su número de DNI y contraseña.
    Los usuarios autenticados reciben un token de acceso y un token de actualización para su
    autenticación futura.

    Atributos:
    - serializer_class: Clase de serialización utilizada para validar las credenciales de inicio de sesión.
    - queryset: Conjunto vacío, no se utilizan datos de la base de datos.
    - permission_classes: Permisos requeridos para acceder a esta vista (permitido para todos).

    Métodos:
    - create: Valida las credenciales de inicio de sesión, autentica al usuario y emite tokens de acceso y actualización.

    """

    serializer_class = serializers.UserLoginSerializer
    queryset = []
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            serializer = serializers.CustomUserSerializer(user)
            token = RefreshToken.for_user(user)
            data = serializer.data
            data["tokens"] = {"refresh": str(
                token), "access": str(token.access_token)}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data='error', status=status.HTTP_400_BAD_REQUEST)


class UserLogoutViewSet(viewsets.ModelViewSet):
    """
    Vista para cerrar la sesión de usuarios.

    Esta vista permite a los usuarios cerrar la sesión al proporcionar un token de actualización
    que se desactiva, lo que invalida los tokens de acceso emitidos anteriormente.

    Atributos:
    - permission_classes: Permisos requeridos para acceder a esta vista (permitido para todos).
    - serializer_class: Clase de serialización utilizada para validar los datos de la solicitud.
    - queryset: Conjunto vacío, no se utilizan datos de la base de datos.

    Métodos:
    - create: Invalida el token de actualización proporcionado, lo que cierra la sesión del usuario.

    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer
    queryset = []

    def create(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
