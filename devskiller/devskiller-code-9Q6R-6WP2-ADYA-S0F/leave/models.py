from enum import IntEnum
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from website import settings
from django.db import models


"""MODEL MANAGER"""
class NewUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_active = True
		user.is_superuser = True
		user.save(using=self._db)
		return user




# class User(AbstractUser):
class User(AbstractBaseUser):
    email 					= models.EmailField(max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    manager                 = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False, verbose_name="admin",)
    is_active				= models.BooleanField(default=True, verbose_name="active",)
    is_verified				= models.BooleanField(default=False, verbose_name="verified",)
    is_staff				= models.BooleanField(default=False, verbose_name="staff",)
    is_superuser			= models.BooleanField(default=False, verbose_name="superuser",)
    language                = models.CharField(max_length=3, default="en")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = NewUserManager()
	
    def __str__(self):
        return self.email 	# For checking permissions. to keep it simple all admin have ALL permissons
	
    def has_perm(self, perm, obj=None):
        return self.is_admin 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
        
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        default_related_name = "org_user"
    

class LeaveRequestStatus(IntEnum):
    open = 0
    accepted = 1
    rejected = 2
    closed = 3


STATUSES = tuple((item.value, item.name) for item in list(LeaveRequestStatus))


class LeaveRequest(models.Model):
    start = models.DateField()
    end = models.DateField()
    request_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="days_off" # "leave.User"
    )
    request_ts = models.DateTimeField(auto_now_add=True) # chaned this to set automatically
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requests" # "leave.User"
    )
    status = models.PositiveSmallIntegerField(
        default=LeaveRequestStatus.open, choices=STATUSES
    )
    review_ts = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.request_by.username + " for @ {self.start} to {self.end}" 

    class Meta:
        verbose_name = "LeaveRequest"
        verbose_name_plural = "LeaveRequests"
