"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import NewAccount
from app.forms import Profilef
from app.forms import loginForm
from django.http import HttpResponseRedirect
import hashlib
import time
from app.models import Profile
import django.contrib.auth.views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

try:
    user
except NameError:
    user = None


def classPage(request):
    """Renders class page"""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/classPage.html',
        {
            'user':user,
        }
    )

def profile(request):
    """Renders profile page"""
    assert isinstance(request,HttpRequest)
    f = Profilef()
    if request.method == 'POST':
        f = Profilef(request.POST)
        if f.is_valid():
            c = f.cleaned_data.get('city')
            pt = f.cleaned_data.get('profileText')
            g = f.cleaned_data.get('grade')
            m = f.cleaned_data.get('major')
            uid = request.session['username']
            uid = User.objects.filter(username=uid)
            try:
                Profile.objects.filter(id=uid).update(city=c)
                Profile.objects.filter(id=uid).update(profileText=pt)
                Profile.objects.filter(id=uid).update(grade=g)
                Profile.objects.filter(id=uid).update(major=m)
            except Exception as ex:
                print(ex)
            return render(
                request,
                'app/index.html',
                {
                    'myForm':f,
                    'user':user,
                }
            )
        else:
            return render(
                request,
                'app/profile.html',
                {
                    'myForm':f,
                    'user':user,
                }
            )
    else:
        return render(
            request,
            'app/profile.html',
            { 
                'myForm':f,
                'user':user,
            }
        )

def newaccount(request):
    """renders account creation page"""
    assert isinstance(request,HttpRequest)
    f = NewAccount()
    if request.method == 'POST':
        f = NewAccount(request.POST)
        if f.is_valid():
            #time.sleep(2)
            p = f.cleaned_data.get('password1')
            uid = f.cleaned_data.get('username')
            fn = f.cleaned_data.get('firstName')
            ln = f.cleaned_data.get('lastName')
            e = f.cleaned_data.get('email')
            b = f.cleaned_data.get('birthday')
            dj = datetime.now()
            ##conver p to bytes
            #bp = p.encode()
            ##encrypt p
            #ep = hashlib.sha512()
            #ep.update(bp)
            #encrypted = ep.digest()
            try:
                newUser = User.objects.create_user(username=uid,password=p,last_login=dj,
                                                   is_superuser=False,first_name=fn,
                                                   last_name=ln,email=e,is_staff=False,
                                                   is_active=True,date_joined=dj)
                #newBday = Profile.objects.filter(username=uid).update(birthday=b)
                if newUser:
                    print("Good")
                    user = authenticate(username=uid, password=p)
                    request.session['username']=uid
                    request.session['user']=user
                    pf = NewAccount()
                    return render(
                        request,
                        'app/profile.html',
                        {
                            'myForm':pf,
                            'user':user,
                        }
                    )

            except Exception as ex:
                print(ex)
            return render(
                request,
                'app/newaccount.html',
                {
                    'myForm':f
                }
            )
        else:
            return render(
                request,
                'app/newaccount.html',
                {
                    'myForm':f
                }
            )
    else:
        return render(
            request,
            'app/newaccount.html',
            { 
                'myForm':f
            }
        )

def recovery(request):
    """Renders account recovery page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/recovery.html',
        {
            'user':user,
        }
    )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'user':user,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact us!',
            'year':datetime.now().year,
            'user':user,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'This app is cool.',
            'year':datetime.now().year,
            'user':user,
        }
    )

def login(request):
    """Renders the login page"""
    assert isinstance(request, HttpRequest)
    lf = loginForm()
    m = request.method
    if m == "GET":
        return render(request,
               'app/login.html',
               {
                   'myForm':lf,
                   'title':'Hello'
               }
        )
    else:
        # POST
        lf = loginForm(request.POST)
        if lf.is_valid(): # validate data
            p = lf.cleaned_data.get('password')
            uid = lf.cleaned_data.get('username')
            user = authenticate(username=uid, password=p)
            if user:
                print('Logged In')
                request.session['username']=uid
                request.session['user']=user
                return render(request,
                       'app/index.html',
                       {
                           'title':'Hello',
                           'user':user,
                       }
                )
            else:
                return render(request,
                       'app/login.html',
                       {
                           'myForm':lf,
                           'title':'Hello'
                       }
                )
