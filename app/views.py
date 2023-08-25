from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_AccessRecord(request):
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_AccessRecord.html',d)

def insert_topic(request):
    tn=input('enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)
def insert_webpage(request):
    tn=input('enter topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
def insert_accessrecord(request):
    pk=int(input('enter pk : '))
    to=Webpage.objects.get(pk=pk)
    to.save()
    d=input('enter date : ')
    a=input('enter author : ')
    e=input('enter email : ')
    ao=AccessRecord.objects.get_or_create(name=to,date=d,author=a,email=e)[0]
    ao.save()
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_AccessRecord.html',d)