from django.shortcuts import render
#importing biodata model
from .models import BioData
from random import randint

# Create your views here.
message = ("you have successfully submited your form")
students = [
    {'id':1,'name':'Adesewa','address':'ondo'},
    {'id':2,'name':'laura','address':'delta'},
    {'id':3,'name':'Eni','address':'lagos'},
]
state = ["ondo","lagos"]
context = BioData.objects.all

def homepage(request):
    
    all_biodata = BioData.objects.all
    return render(request,'home.html',{'all': all_biodata} )

def service(request):
    return render(request,'service.html',context)

def studentinfo(request,param):
    student =  None
    for i in BioData.objects.all():
        if i.id == int(param):
            student = i
    return render(request,'student.html',{'student':student})

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname  = request.POST['lname']
        address = request.POST['address']
        age = request.POST['age']
        nin = randints(10)
        atm = randints(15)
    
        new_bio = BioData(fname=fname,lname=lname,address=address,age=age,nin=nin,atm=atm)
        new_bio.save()
        if new_bio.save():
           print(message)
    return render(request,'register.html')


def randints(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start,range_end)

def atms(f):
    range_start = 15**(f-1)
    range_end = (15**f)-1
    return randint(range_start,range_end)

def view_all(request):
    context = BioData.objects.all()
    return render(request, 'view_all.html', {'all':context})