from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class Manager(AbstractUser):
	'''
	Change existing user models
	Remove username and make email as Usernamefield
	Add required field
	'''
	username 	= None
	email 		= models.EmailField(_('email address'), unique=True) # unique Email
	address 	= models.TextField()
	dob 		= models.DateField()
	company 	= models.CharField(max_length=50)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['first_name','last_name','address','dob','company']

	objects = CustomUserManager() # User Coustom Manager 

	def __str__(self):
		return self.email