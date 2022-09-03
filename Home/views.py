from django.shortcuts import render,HttpResponse
from Home.models import Contact
from Home.models import About
from Home.models import Homee
from Home.models import Teamm



# Create your views here.

def Home(request):
    homes=Homee.objects.all()
    print(homes)
    return render(request,'home.html',{'homes':homes})


def Contactus(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        message= request.POST['message']
        ins = Contact(name=name,email=email,address=address,message=message)
        ins.save()
        
    return render(request,'contactus.html')    



def Aboutus(request):
    abouts =About.objects.all()
    return render(request,'aboutus.html',{'abouts':abouts}) 
       




def Team(request):
    teams= Teamm.objects.all()
    return render(request,'team.html',{'teams':teams})