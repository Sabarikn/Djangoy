from django import forms

from .models import Login,Converter1

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
class LoginForm(forms.ModelForm):
 	password = forms.CharField(widget = forms.PasswordInput)
 	# fullname = forms.CharField(max_length=120,blank=False)
 	class Meta:
 		model = Login
 		fields = ['fullname','password']
class Converter(forms.ModelForm):
	amount = forms.IntegerField(required = True,label = 'value')
	class Meta:
		model=Converter1
		fields=['convertfrom','convertto','amount']
	def clean(self):
		return self.cleaned_data

	# status=((1,"INR"),
	# 	(2,"USD"),
	# 	(3,"EUR"),
	# 	(4,"GBP"),
	# 	(5,"SGB"))
	# convertfrom = forms.ChoiceField(
	# 	choices=status,
	# 	required = True,
	# 	label = 'convertfrom'
	# )
	# convertto = forms.ChoiceField(
	# 	choices=status,
 #    	required = True,
 #    	label = 'convertto')
	# amount = forms.IntegerField(required = True,label = 'value')
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )