from django import forms

from .models import Love

class ContactForm(forms.Form):
	fullname = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()



	
class SignUpForm(forms.ModelForm):
	class Meta:
		model = Love
		fields = ['fullname', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		print(email)
		if not "edu" == email.split('.')[-1]:
			raise forms.ValidationError("please use a valid .edu email address")
		return email