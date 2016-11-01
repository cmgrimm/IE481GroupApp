"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import NewAccount
from app.forms import Profile
from django.http import HttpResponseRedirect


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
    fp = Profile()
    return render(
        request,
        'app/profile.html',
        { 
            'profileTable':fp
        }
    )

def newaccount(request):
    """renders account creation page"""
    assert isinstance(request,HttpRequest)
    f = NewAccount()
    if request.method == 'POST':
        return HttpResponseRedirect('profile')
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
