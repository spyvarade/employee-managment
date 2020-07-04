from django.db import models
from phone_field import PhoneField



class Employee(models.Model):
	'''
	 	Employee Models manage by Manager
	'''

	email 		= models.EmailField(unique=True)
	first_name 	= models.CharField(max_length=50)
	last_name  	= models.CharField(max_length=50)
	city 		= models.CharField(max_length=50)
	address 	= models.TextField()
	dob     	= models.DateField()
	phone 		= PhoneField(help_text='Contact phone number')


	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)


	class Meta:
		ordering = ['first_name']

