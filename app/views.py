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
from app.forms import newclass
from app.forms import messageForm
from app.forms import addClass
from django.http import HttpResponseRedirect
import hashlib
import time
from app.models import Profile
from app.models import enrollment
from app.models import classSection
from app.models import Message
from django.contrib import messages
import django.contrib.auth.views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

try:
    user
except NameError:
    user = None

def messages(request):
    """Renders newCLass page"""
    assert isinstance(request,HttpRequest)
    f = messageForm()
    username = request.session['username']
    classes = enrollment.objects.filter(username=username).values('classSec')
    choice = []
    for v in classes:
        print(v)
        choice.append(v.values())
    data = enrollment.objects.filter(classSec__in=classes).order_by('classSec')
    inbox = Message.objects.filter(receiver=username).order_by('-created_at')
    if request.method == "POST":
        f = messageForm(request.POST)
        if f.is_valid():
            re = f.cleaned_data.get('receiver')
            sub = f.cleaned_data.get('subject')
            cont = f.cleaned_data.get('contents')
            sdr = username
            snt = datetime.today()
            users = User.objects.filter(username=re).values('username')
            uns = list(users.values())
            #for v in users:
            #    print(v)
            #    uns.append(list(v.values()))
            #endfor
            try:
                newMsg = Message.objects.create(sender=sdr,receiver=re,subject=sub,msg_content=cont,created_at=snt)
            except Exception as ex:
                print(ex)
                #messages.add_message(request, messages.error, 'Message not sent:'+ex)
            return render(
                request,
                'app/messages.html',
                {
                    'myForm':f,
                    'data':data,
                    'inbox':inbox,
                    #'messages':message
                }
            )
        return render(
            request,
            'app/messages.html',
            {
                'myForm':f,
                'data':data,
                'messages':messages,
                'inbox':inbox,
            }
        )
    else:
        return render(
            request,
            'app/messages.html',
            {
                'myForm':f,
                'data':data,
                'messages':messages,
                'inbox':inbox,
            }
        )

def newClass(request):
    """Renders newCLass page"""
    assert isinstance(request,HttpRequest)
    f = newclass()
    data = classSection.objects.all()
    if request.method == "POST":
        f = newclass(request.POST)
        if f.is_valid():
            class1 = f.cleaned_data.get('class1')
            section = f.cleaned_data.get('section')
            day = f.cleaned_data.get('day')
            time1 = f.cleaned_data.get('time1')
            classSec = "%s_%s" % (class1,section)
            try:
                newClass = classSection.objects.create(classSec=classSec,class1=class1,section=section,day=day,classTime=time1)
            except Exception as ex:
                print(ex)
            return render(
                request,
                'app/newClass.html',
                {
                    'myForm':f,
                    'data':data,
                }
            )
        return render(
            request,
            'app/newClass.html',
            {
                'myForm':f,
                'data':data,
            }
        )
    else:
        return render(
            request,
            'app/newClass.html',
            {
                'myForm':f,
                'data':data,
            }
        )

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
        print(request.POST)
        f = Profilef(request.POST)
        if f.is_valid():
            c = f.cleaned_data.get('city')
            pt = f.cleaned_data.get('profileText')
            g = f.cleaned_data.get('grade')
            m = f.cleaned_data.get('major')
            uid = request.session['username']
            uid = User.objects.filter(username=uid).values('id')
            try:
                Profile.objects.filter(id=uid).update(city=c)
                Profile.objects.filter(id=uid).update(profileText=pt)
                Profile.objects.filter(id=uid).update(grade=g)
                Profile.objects.filter(id=uid).update(major=m)
            except Exception as ex:
                print(ex)
            nid = User.objects.filter(username=uid).values('id')
            try:
                data = enrollment.objects.filter(username=uid).values('classSec')
            except:
                data=''
            classChoice = classSection.objects.all().values('classSec')
            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'data':data,
                    'classes':classChoice,
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
                nid = User.objects.filter(username=uid).values('id')
                newBday = Profile.objects.filter(id=nid).update(birthday=b)
                if newUser:
                    print("Good")
                    #user = authenticate(username=uid, password=p)
                    request.session['username']=uid
                    request.session['user']=user
                    pf = Profilef()
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
    f = addClass()
    if request.method == "POST":
        cf = addClass(request.POST)
        if cf.is_valid():
            username = request.session['username']
            nc = "%s" % (request.POST.get('addclass'))
            uc = "%s_%s" % (username, nc)
            try:
                addclass = enrollment.objects.create(classSec=nc,username=username,uc=uc)
            except:
                print("Already registered")
            try:
                data = enrollment.objects.filter(username=username).values('classSec')
            except:
                data=''
            classChoice = classSection.objects.all().values('classSec')
            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'data':data,
                    'classes':classChoice,
                    'myForm':f,
                }
            )
        else:
            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'user':user,
                    'myForm':f,
                }
            )
    else:
        if 'username' in request.session:
            username = request.session['username']
            nid = User.objects.filter(username=username).values('id')
            try:
                data = enrollment.objects.filter(username=username).values('classSec')
            except:
                data=''
            classChoice = classSection.objects.all().values('classSec')
            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'data':data,
                    'classes':classChoice,
                    'myForm':f,
                }
            )
        else:
            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
                    'user':user,
                    'myForm':f,
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
            uid=lf.cleaned_data.get('username')
            p=lf.cleaned_data.get('password')
            user = True #authenticate(username=uid, password=p)
            if user:
                request.session['username']=uid
                request.session['user']=user
                username=uid
                try:
                    data = enrollment.objects.filter(username=username).values('classSec')
                except:
                    data=''
                classChoice = classSection.objects.all().values('classSec')
                print('Logged In')
                f=addClass()
                return render(
                    request,
                    'app/index.html',
                    {
                        'title':'Home Page',
                        'year':datetime.now().year,
                        'data':data,
                        'classes':classChoice,
                        'myForm':f,
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
