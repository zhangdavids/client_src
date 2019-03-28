from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class PersonManager(BaseUserManager):
    def create_user(self, email, date_of_birth, username, password=None):
        # if not email:
        #     msg = 'Users must have an email address'
        #     raise ValueError(msg)

        if not username:
            msg = 'This username is not valid'

            raise ValueError(msg)

        # if not date_of_birth:
        #     msg = 'Please Verify Your DOB'
        #     raise ValueError(msg)

        user = self.model(email=PersonManager.normalize_email(email),
                          username=username,
                          date_of_birth=date_of_birth)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, date_of_birth):
        user = self.create_user(email, password=password, username=username, date_of_birth=date_of_birth)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not username:
            raise ValueError('The given username must be set')
        username = username
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class SysUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the username
        """

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser
        """
        user = self.create_user(username, password)

        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class UserProfile(AbstractUser):
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(u'username', max_length=32, unique=True)
    token = models.CharField(u'token', max_length=128, default=None, blank=True, null=True)
    department = models.CharField(u'部门', max_length=32, default=None, blank=True, null=True)
    mobile = models.CharField(u'手机', max_length=32, default=None, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True, null=True, default=None)
    dep = models.CharField('Department', max_length=128, blank=True)
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    nick_name = models.CharField(max_length=50, verbose_name=u"""昵称""", default="""""")
    birthday = models.DateField(verbose_name=u"""生日""", null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(("""male""", u"""男"""), ("""female""", u"""女""")),
                              default="""female""")
    address = models.CharField(max_length=100, default=u"""""")
    image = models.ImageField(upload_to="""image/%Y/%m""", default=u"""image/default.png""", max_length=100)

    mod_date = models.DateTimeField('Last modified', auto_now=True)
    create_date = models.DateTimeField('created time', auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = SysUserManager()

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.username
