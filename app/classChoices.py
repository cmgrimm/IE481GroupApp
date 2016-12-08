from app.models import enrollment

def getChoices(request):
    username = request.session['username']
    classchoices = enrollment.objects.filter(username=username).values('classSec')
    choice = None
    for v in classchoices:
        choice = choice,v.classSec
