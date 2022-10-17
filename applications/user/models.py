from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, fullname,dni, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            fullname = fullname,
            dni= dni,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, fullname,dni, password=None, **extra_fields):
        return self._create_user(username, email, fullname, dni, password, False, False, **extra_fields)

    def create_superuser(self, username, email, fullname,dni, password=None, **extra_fields):
        return self._create_user(username, email, fullname,dni, password, True, True, **extra_fields)


class Role(models.Model):
    class Meta:
        verbose_name= 'Roles - Sentidos'
        verbose_name_plural = 'Roles - Sentidos Restaurante y Casa de Te.'

    name = models.CharField("Nombre de Rol", max_length=50, unique=True)
    description = models.CharField("Descripcion del rol", max_length=120)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Usuario", max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    fullname = models.CharField('Nombre Completo', max_length = 255)
    dni = models.IntegerField("DNI")
    role = models.ForeignKey(Role, on_delete= models.CASCADE, null=True, blank=True, verbose_name="Rol")
    is_staff = models.BooleanField(default = True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario registrado - Restaurante Sentidos.'
        verbose_name_plural = 'Usuarios registrados - Restaurante Sentidos.'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','fullname','dni']

    def __str__(self):
        return f'{self.username}'
