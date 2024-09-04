from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from enum import Enum



class UserRole(Enum):
    USER='user'
    ADMIN='admin'
    SUPERADMIN='superadmin'


class CustomUserManager(BaseUserManager):
    def create_user(self,email, role=UserRole.USER,password=None,**extra_fields):
        if not email:
            raise ValueError(_("Email required"))
        email=self.normalize_email(email)
        user=self.model(email=email,role=role,**extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("role",UserRole.SUPERADMIN.value)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password=password, **extra_fields)