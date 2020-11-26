from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
	first_name =  models.CharField(max_length=123, null=True)
	last_name =  models.CharField(max_length=123, null=True)
	email =  models.EmailField(null=True)
	phone_number = models.IntegerField()
	passport = models.ImageField(upload_to='passport_pic', blank=True)
	country =  models.CharField(max_length=123, null=True)
	address =  models.CharField(max_length=123, null=True)
	next_of_kin_name =  models.CharField(max_length=123, null=True)
	next_of_kin_email =  models.EmailField(null=True)

	def get_absolute_url(self):
		return reverse ('basic_app:detail', kwargs={'pk':self.pk})

	def __str__(self): 
		name = f'{self.last_name} {self.first_name}'
		return name