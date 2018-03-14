from django import forms

from .models import Tweet

# class ContactForm(forms.Form):
# 	fullname = forms.CharField()
# 	email = forms.EmailField()
# 	message = forms.CharField()



	
# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = Love
# 		fields = ['fullname', 'email']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		print(email)
# 		if not "edu" == email.split('.')[-1]:
# 			raise forms.ValidationError("please use a valid .edu email address")
# 		return email
class TweetForm(forms.ModelForm):
 	 # fullname = forms.CharField(max_length=120,blank=False)
 	class Meta:
 		model = Tweet
 		fields = ['fullname']
 	# def clean(self):
 	# 	try:
 	# 		if self.cleaned_data['fullname'] and self.cleaned_data['password']:
 	# 			username = self.cleaned_data['fullname']
 	# 			userpassword = self.cleaned_data['password']
 	# 	except KeyError:
 	# 		raise forms.ValidationError('Please enter full details')

 		
 		# if not re.search(r'^\w+$', username):
 		# 	raise forms.ValidationError('Wrong username')
 		# try:
 		# 	Signup.objects.get(fullname = username)
 		# except ObjectDoesNotExist:
 		# 	raise forms.ValidationError('Username or Password incorrect ')
 		# if userpassword == Signup.objects.get(fullname = username).password1 :
 		# 	return self.cleaned_data
 		# else:
 		# 	raise forms.ValidationError('Username or Password incorrect ')