from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True): # takes all the fields which are specified in REQUIRED_FIELDS
		if not email:
			raise ValueError("User must have an email address")
		if not password:
			raise ValueError("User must have a password")	
		user_obj = self.model(
			email = self.normalize_email(email)
		)
		user_obj.set_password(password) # used to set and also to change user password
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj	

	def create_staffuser(self, email, password=None):
		user = self.create_user(
				email,
				password = password,
				is_staff = True
		)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None):
		user = self.create_user(
				email = self.normalize_email(email),
				password = password,
				is_staff = True,
				is_admin = True
		)
		user.save(using=self._db)
		return user



class User(AbstractBaseUser):
	email 			= models.EmailField(max_length=255, unique=True)
	full_name 		= models.CharField(max_length=255, blank=True, null=True)
	active 			= models.BooleanField(default=True)
	staff 			= models.BooleanField(default=False)
	admin 			= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	email_confirmed = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] 

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_fullname(self):
		return

	def shortname(self):
		return

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_lebel):
		return True


	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active


# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	email_confirmed = models.BooleanField(default=False)

# 	def __str__(self):
# 		return f'{self.user.full_name} Profile'

# 	# def save(self, *args, **kwargs):
#  #        super(Profile, self).save(*args, **kwargs)	
		