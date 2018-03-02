from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import LoginForm,UserRegistrationForm,Converter
from django import forms
import requests
import ast
from django.contrib.auth.models import User
# Create your views here. 
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
def login1(request):
	form = LoginForm(request.POST or None )
	title="Welcome "
	context = {
		"template_title": title,
		"form": form,
	    }
	#if request.user.is_authenticated():
	#	title="I LOVE %s"%(request.user)
	
	# print(request)
	# if request.method=="POST":
	# print(request.POST)
	if form.is_valid():
		print(request,form.cleaned_data)
		userObj=form.cleaned_data
		username = userObj['username']
		password =  userObj['password']
		try:
			user=authenticate(username = username, password = password)
			login(request,user)
			return HttpResponseRedirect('/currency')
		except:
			return HttpResponseRedirect('currency/login')
		# instance = form.save(commit=False)
		# fullname=form.cleaned_data.get('fullname')
		# if not fullname:
		# 	fullname="new full MH"
		# instance.fullname=fullname
		# # if not instance.fullname:
		# # 	instance.fullname="saab"
		# # print(instance)
		# instance.save()
		# context = {
		# "template_title": "Thanku"
		# ""
	 #    }
		
	return render(request,"registration/login.html",context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/currency')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/registration.html', {'form' : form})




def home(request):
    return render(request, 'registration/home.html')

def converter(request):
	if request.method=='POST':
		form=Converter(request.POST)
		cfrom = request.POST.get('convertfrom')
		cto = request.POST.get('convertto')
		amnt = (request.POST.get('amount'))
		print(cfrom,cto,amnt)
		response=requests.get("https://api.fixer.io/latest?base="+cfrom)
		text=ast.literal_eval(response.text)
		rates=text['rates']
		print((rates[cto]))
		amount =(rates[cto])*(float(amnt))

		prnt="THE AMOUNT IS:"+str(amount)

	else:
		prnt="Please Select The exchange rates"
		form=Converter()
	return render(request,'registration/converter.html',{"print":prnt,"form":form})