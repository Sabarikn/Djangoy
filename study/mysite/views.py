from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.conf import settings
from django.shortcuts import render
from .forms import AddForm
from .models import Leaderboard
# Create your views here.

def home(request):
    return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         print(request)
#         if form.is_valid():
#             userObj = form.cleaned_data
#             username = userObj['username']
#             email =  userObj['email']
#             password =  userObj['password']
#             if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
#                 User.objects.create_user(username, email, password)
#                 user = authenticate(username = username, password = password)
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 raise forms.ValidationError('Looks like the username  already exists')


#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register.html', {'form' : form})
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        print(request)
        if form.is_valid():
            context = {
            "title": "Please Enter Student Name And Marks",
            "form": form
            }
            form.cleaned_data['userid'] = request.user.id
            print(form.cleaned_data)
            instance = form.save(commit=False)
            instance.userid=request.user.id
            instance.save()
            return render(request,"home.html",context)
        

    # if form.is_valid() and request.user.is_authenticated():
    #     context = {
    #         "title": "Please Enter Student Name And Marks",
    #         "form": form
    #         }
    #     form.cleaned_data['userid'] = request.user.id
    #     print(form.cleaned_data)
    #     instance = form.save(commit=False)
    #     instance.userid=request.user.id
    #     instance.save()
    else:
        form = AddForm()
        context = {
            "form":form
            }
    return render(request,"add.html",context)




def delete(request,pk):
    print(request,"\n",pk,"\n",request.user.id)
    le1=Leaderboard.objects.get(id=pk)
    le=le1.userid
    print(le)
    if int(request.user.id) == int(le):
        message="Deleted"
        Leaderboard.objects.filter(id=pk).delete()
    else:
        message="Unsuccessfull cannot delete other's data"
    le2=Leaderboard.objects.all()
    context={
        "title":message,
        "leaderboard":le2
        }
    
    return render(request,"leaderboard.html",context)

# def home1(request):
#     # form = SignUpForm(request.POST or None )
#     title="Welcome To Leaderboard"
#     context={
#         "template_title": title
#         }
#     return render(request,"leaderboard.html",context)



def show(request):
    # lead = [(i.name,i.marks,i.userid) for i in Leaderboard.objects.all()]
    le=Leaderboard.objects.all()
    context={
        "title": "hhhooo",
        "leaderboard":le
        }
    
    return render(request,"leaderboard.html",context)