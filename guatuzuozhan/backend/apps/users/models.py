from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Manager compatible with Django auth without creating a new user table."""

    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The name must be set')
        user = self.model(name=name, **extra_fields)
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        if not password:
            raise ValueError('Superusers must have a password')
        extra_fields.setdefault('is_system_admin', True)
        extra_fields.setdefault('is_deleted', False)
        user = self.create_user(name, password, **extra_fields)
        return user


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    class Meta:
        managed = False
        db_table = 'departments'

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, db_column='department_id', on_delete=models.DO_NOTHING, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    responsibility = models.TextField(null=True, blank=True)
    is_system_admin = models.BooleanField()
    account_status = models.CharField(max_length=20)
    register_status = models.CharField(max_length=20)
    reviewer_id = models.BigIntegerField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    review_remark = models.TextField(null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField()
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'users'
    @property
    def is_active(self): return not self.is_deleted

    @property
    def is_authenticated(self): return True

    @property
    def is_anonymous(self): return False

    @property
    def is_staff(self): return self.is_system_admin

    @property
    def is_superuser(self): return self.is_system_admin

    def set_password(self, raw_password): self.password_hash = make_password(raw_password)
    def check_password(self, raw_password): return check_password(raw_password, self.password_hash)
