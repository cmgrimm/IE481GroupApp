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

def classPage(request):
    """Renders class page"""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/classPage.html',
    )

def profile(request):
    """Renders profile page"""
    assert isinstance(request,HttpRequest)
    f = Profilef()
    if request.method == 'POST':
        f = Profilef(request.POST)
        if f.is_valid:
            time.sleep(2)
            c = f.cleaned_data.get('city')
            pt = f.cleaned_data.get('profileText')
            g = f.cleaned_data.get('grade')
            m = f.cleaned_data.get('major')
            try:
                Profile.objects.filter(username=uid).update(city=c)
                Profile.objects.filter(username=uid).update(profileText=pt)
                Profile.objects.filter(username=uid).update(grade=g)
                Profile.objects.filter(username=uid).update(major=m)
            except Exception as ex:
                print(ex)
            return render(
                request,
                'app/index.html',
                {
                    'myForm':f
                }
            )
        else:
            return render(
                request,
                'app/profile.html',
                {
                    'myForm':f
                }
            )
    else:
        return render(
            request,
            'app/profile.html',
            { 
                'myForm':f
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
                newBday = Profile.objects.filter(username=uid).update(birthday=b)
                if newUser:
                    print("Good")
                    user = authenticate(username=uid, password=p)
                    request.session['username']=uid
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
        'app/recovery.html'
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
            uid=request.POST.get('username')
            p=request.POST.get('password')
            user = authenticate(username=uid, password=p)
            if user:
                print('Logged In')
                request.session['username']=uid
                request.user=user
                return render(request,
                       'app/index.html',
                       {
                           'title':'Hello'
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
