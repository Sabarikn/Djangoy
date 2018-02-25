from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import AddForm
from .models import Leaderboard


# from app.forms import *
# Create your views here. 
def home(request):
	# form = SignUpForm(request.POST or None )
	title="Welcome To Leaderboard"
	context={
		"template_title": title
		}
	return render(request,"leader.html",context)
	#if request.user.is_authenticated():
	#	title="I LOVE %s"%(request.user)
	
	# print(request)
	# if request.method=="POST":
	# print(request.POST)
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	fullname=form.cleaned_data.get('fullname')
	# 	if not fullname:
	# 		fullname="new full MH"
	# 	instance.fullname=fullname
	# 	# if not instance.fullname:
	# 	# 	instance.fullname="saab"
	# 	# print(instance)
	# 	instance.save()
	# 	context = {
	# 	"template_title": "Thanku"
	# 	""
	#     }
		
	


def add(request):
	form = AddForm(request.POST or None )

	if form.is_valid() and request.user.is_authenticated():
		context = {
			"title": "Please Enter Student Name And Marks",
			"form": form
			}
		form.cleaned_data['userid'] = request.user.id
		print(form.cleaned_data)
		instance = form.save(commit=False)
		instance.userid=request.user.id
		instance.save()
	else:
		context = {
			"title": "Please Login or register to add detaails"
			}

	return render(request,"add.html",context)




def show(request):
	# lead = [(i.name,i.marks,i.userid) for i in Leaderboard.objects.all()]
	le=Leaderboard.objects.all()
	if request.user.is_authenticated():
		context={
		"leaderboard":le,
		"userid": request.user.id
		}
	else:
		context={
		"leaderboard":le
		}
	
	return render(request,"leaderboard.html",context)



# def login(request):
# 	form = LoginForm(request)
# 	context = {
# 	"title": "Please Enter Valid Details",
# 	"form": form
# 	}
# 	if
# 	return render(request,"login.html",context)

# def contact(request):

# 	form = ContactForm(request.POST or None)
# 	if form.is_valid():
# 		# for key,value in form.cleaned_data.items():
# 		# 	print(key,value)
# 		form_email=form.cleaned_data.get('email')
# 		form_fullname=form.cleaned_data.get('fullname')
# 		form_message=form.cleaned_data.get('message')
# 		subject = "site contact"
# 		from_email = settings.EMAIL_HOST_USER
# 		to_email = [from_email,"123sabari456@gmail.com"]
# 		contact_message = "%s : %s via %s"%(
# 			form_fullname,
# 			form_message,
# 			form_email) 
# 		send_mail(subject,
# 				contact_message,
# 				from_email,
# 				[to_email],
# 				fail_silently=False)

# 		# print(email,fullname,message)
# 	context = {
# 	"template_title": "Melcow",
# 	"forms": form,
# 		}

# 	return render(request,"forms.html",context)