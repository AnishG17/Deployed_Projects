from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
class Branch(models.Model):
	branch = models.CharField(max_length=50)     # Branch of that phone model

	def __str__(self):
		return self.branch

   
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)        # user name
    contact = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10)       # user phone number
    email  = models.EmailField(max_length=50)                       # user email id

    def __str__(self):
        return str(self.user)

class Phone(models.Model):
    name = models.CharField(max_length=50)       # Name of Phone
    image = models.ImageField(upload_to="")      # Images on Phone
    price = models.IntegerField(default=0)       # Price
    desc = models.TextField(max_length = 500)    # Contains all specifications of phone model
    branchPhone = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)                                                                  # Which branch are there for specific          
                                                                                     
    def __str__(self):
        return self.name

# class Color(models.Model):
# 	color = ColorField(default=’#FF0000’)       # Contains color of Phone
# 	colorPhone = models.ForeignKey(Phone, on_delete=models.CASCADE)
#                                                 # Store which phone has which color
# 	def __str__(self):
# 		return self.color




