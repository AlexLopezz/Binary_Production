from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, username, email, fullname,dni,role, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            fullname = fullname,
            dni= dni,
            role = role,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, fullname,dni,role, password=None, **extra_fields):
        return self._create_user(username, email, fullname, dni,role, password, False , False, **extra_fields)

    def create_superuser(self, username, email, fullname,dni,role=None, password=None, **extra_fields):
        return self._create_user(username, email, fullname,dni,role, password, True, True, **extra_fields)
        
