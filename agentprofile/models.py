from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User already registered with this email.')
        
        user = self.model(email=self.normalize_email(email), password=make_password(password))
        user.save(using=self._db)
            
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class UserBase(AbstractBaseUser):
    id = models.AutoField(primary_key=True)    
    email = models.EmailField(max_length=255, unique=True)

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserProfileManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True

    def get_full_name(self):
        # Get full name
        return self.fname + ' ' + self.lname
    
    def get_short_name(self):
        # Get only the first name (for design purposes)
        return self.fname

    def __str__(self):
        return self.email


class AgentProfile(UserBase):
    objects = UserProfileManager()

