import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ms_id = models.UUIDField(default=uuid.uuid4, editable=False,null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    role = models.CharField(_("role"), max_length=20, choices=[
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superadmin', 'Superadmin'),
    ], default='user')
    mobile = models.CharField(_("Mobile"), max_length=150, blank=True, null=True)
    office_location = models.CharField(_("Office Location"), max_length=150, blank=True, null=True)
    job_title = models.CharField(_("Job Title"), max_length=150, blank=True, null=True)
    preferred_language = models.CharField(_("Preferred Language"), max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True) 

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table='users'

    def __str__(self):
        return self.email
