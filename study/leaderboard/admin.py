from django.contrib import admin

# Register your models here.
from .forms import AddForm

from .models import Leaderboard
class AddAdmin(admin.ModelAdmin):
	list_display=["__unicode__","userid"]
	form=AddForm
	#class Meta:
	#	model=Love
admin.site.register(Leaderboard,AddAdmin)