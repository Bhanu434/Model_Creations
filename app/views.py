from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)
def display_webpages(request):
    QLWO=Webpages.objects.all()
    d={'QLWO':QLWO}
    return render (request,'display_webpages.html',d)
def display_accessrecords(request):
    QLAO=AccessRecords.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'display_accessrecords.html',d)
def insert_topic(request):
    tn=input('Enter Your Topic Name :- ')
    nto=Topic.objects.get_or_create(topic_name=tn)[0]
    nto.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)
def insert_webpages(request):
    tn=input('Enter Your Topic Name :- ')
    n=input('Enter Your Name :- ')
    url=input('Enter Your Url :- ')
    Email=input('Enter Your Email :- ')
    TO=Topic.objects.get(topic_name=tn)
    WO=Webpages.objects.get_or_create(topic_name=TO,name=n,url=url,Email=Email)[0]
    WO.save()
    QLWO=Webpages.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)
def insert_accessrecords(request):
    n=input('Enter Your Name :- ')
    d=input('Enter Date ex:yyyy-mm-dd :- ')
    a=input('Enter Your Author Name :- ')
    no=Webpages.objects.get(name=n)
    ARO=AccessRecords.objects.get_or_create(name=no,date=d,Author=a)[0]
    ARO.save()
    QLAO=AccessRecords.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'display_accessrecords.html',d)

