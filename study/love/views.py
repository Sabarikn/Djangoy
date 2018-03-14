from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import TweetForm
from django import forms

# Create your views here. 
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
import requests,ast,json
from requests_oauthlib import OAuth1Session


API_KEY = "p9fKktOiQSRqQQMEnG3cWQBc3"
API_SECRET = "w4P0lBXG4JrEI7UT5mPy9AXgefFlSNJWhmYVRmNfmp2bHjg7Zw"
test = OAuth1Session(API_KEY,API_SECRET)
def tweets(request):
	if request.method=='POST':
		form=TweetForm(request.POST)
		username = request.POST.get('fullname')
		user_timeline= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=7"
		r = test.get(user_timeline)
		tweets = json.loads(r.text)
		head =   "Tweets"
		prnt = []
		for i in tweets:
			prnt.append(i["created_at"]+"\n"+i["text"])

	else:
		head = ""
		prnt=""
		form=TweetForm()
	context = {"form":form,"print" : prnt,"head":head}
	return render(request,'login.html',context)
# def login1(request):
# 	form = LoginForm(request.POST or None )
# 	title="Welcome "
# 	context = {
# 		"template_title": title,
# 		"form": form,
# 	    }
# 	#if request.user.is_authenticated():
# 	#	title="I LOVE %s"%(request.user)
	
# 	# print(request)
# 	# if request.method=="POST":
# 	# print(request.POST)
# 	if form.is_valid():
# 		userObj=form.cleaned_data
# 		username = userObj['fullname']
# 		password =  userObj['password']
# 		try:
# 			user=authenticate(username = username, password = password)
# 			login(request,user)
# 			return HttpResponseRedirect('/')
# 		except:
# 			return HttpResponseRedirect('/login1')
# 		# instance = form.save(commit=False)
# 		# fullname=form.cleaned_data.get('fullname')
# 		# if not fullname:
# 		# 	fullname="new full MH"
# 		# instance.fullname=fullname
# 		# # if not instance.fullname:
# 		# # 	instance.fullname="saab"
# 		# # print(instance)
# 		# instance.save()
# 		# context = {
# 		# "template_title": "Thanku"
# 		# ""
# 	 #    }
		
# 	return render(request,"forrms.html",context)



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