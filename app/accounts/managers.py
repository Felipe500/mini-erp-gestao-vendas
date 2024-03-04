from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from app.common.choices import TYPE_USER

from app.common.models import SoftDeletionManager


class UserManager(BaseUserManager, SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop("type", TYPE_USER.employee)
        print(self.type)
        super().__init__(*args, **kwargs)

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("type", 'admin')
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

    def create_employee(self, email, password=None, **kwargs):
        request = None
        if 'request' in kwargs:
            request = kwargs.pop('request')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        self.add_ip_agent(user, request)
        user.type = TYPE_USER.employee
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_user_type(self, type=None):
        return super().get_queryset().filter(type__in=self.type)

    def get_collaborator(self, type=None):
        return super().get_queryset().filter(type='employee')
