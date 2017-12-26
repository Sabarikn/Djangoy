from django.contrib import admin

# Register your models here.
from .forms import SignUpForm

from .models import Love
class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","time","updated"]
	form=SignUpForm
	#class Meta:
	#	model=Love
admin.site.register(Love,SignUpAdmin)