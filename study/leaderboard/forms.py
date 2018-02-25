import re
from django import forms
from .models import Leaderboard
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class AddForm(forms.ModelForm):
	class Meta:
		model = Leaderboard
		fields = ['name','marks']
	def clean(self):
		pass
	




	
# class SignUpForm(forms.ModelForm):
# 	password1 = forms.CharField(widget = forms.PasswordInput)
# 	password2 = forms.CharField(widget = forms.PasswordInput)
# 	class Meta:
# 		model = Signup
# 		fields = ['fullname','Sex','email','password1','password2']
# 	def clean_fullname(self):
# 		username = self.cleaned_data['fullname']
# 		if not re.search(r'^\w+$', username):
# 			raise forms.ValidationError('Username can only contai alphanumeric characters and the underscore.')
# 		try:
# 			Signup.objects.get(fullname = username)
# 		except ObjectDoesNotExist:
# 			return username
# 		raise forms.ValidationError('Username is already taken.')

# 	# def clean_fullname(self):
# 	# 	try:
# 	# 		user = User.objects.get(username=self.cleaned_data['fullname'])
# 	# 	except User.DoesNotExist:
# 	# 		return self.cleaned_data['fullname']
# 	# 	raise forms.ValidationError(_("The username already exists. Please try another one."))

# 	def clean(self):	
# 		try:
# 			if self.cleaned_data['password1'] and self.cleaned_data['password2']:
# 				if self.cleaned_data['password1'] != self.cleaned_data['password2']:
# 					raise forms.ValidationError("Passwords doesn't match")
# 			return self.cleaned_data
# 		except KeyError:
# 			raise forms.ValidationError("enter both passwords")

# 	# def clean(self):
#  #    	if self.cleaned_data['password1'] and self.cleaned_data['password2']:
#  #    		if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#  #    			raise ValidationError("Passwords doesn't match")
#  #    	return self.cleaned_data
# class LoginForm(forms.ModelForm):
#  	password = forms.CharField(widget = forms.PasswordInput)
#  	class Meta:
#  		model = Login
#  		fields = ['fullname','password']
#  	def clean(self):
#  		try:
#  			if self.cleaned_data['fullname'] and self.cleaned_data['password']:
#  				username = self.cleaned_data['fullname']
#  				userpassword = self.cleaned_data['password']
#  		except KeyError:
#  			raise forms.ValidationError('Please enter full details')

#  		if not re.search(r'^\w+$', username):
#  			raise forms.ValidationError('Wrong username')
#  		try:
#  			Signup.objects.get(fullname = username)
#  		except ObjectDoesNotExist:
#  			raise forms.ValidationError('Username or Password incorrect ')
#  		if userpassword == Signup.objects.get(fullname = username).password1 :
#  			return self.cleaned_data
#  		else:
#  			raise forms.ValidationError('Username or Password incorrect ')



		 
		

