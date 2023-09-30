from django.shortcuts import render
from .models import reg_tbl,pro_tbl



# Create your views here.
def home(request):
    return render(request,"home.html")

def reg(request):
    if request.method=='POST':
        usn = request.POST.get('un')    
        eml = request.POST.get('em')  
        ps1 = request.POST.get('ps') 
        obj = reg_tbl.objects.create(uname=usn,email=eml,pass1=ps1)
        obj.save()
        if obj:
            return render(request,"login.html")
        else:
            return render (request,"regform.html")
    else:
        return render (request,"regform.html")   
    
def log(request):
    if request.method=='POST': 
        eml = request.POST.get('em')
        psw = request.POST.get('ps')  
        obj=reg_tbl.objects.filter(email=eml,pass1=psw)
        if obj:
            return render(request,"home.html")
        else:
            msg="Invalid Email Id And Password"
            return render (request,"login.html",{"error":msg})

    else:
        return render (request,"login.html")       


def pro(request):
    if request.method=='POST':
        usn = request.POST.get('un')    
        eml = request.POST.get('em')  
        adrs = request.POST.get('ads') 
        pict = request.POST.get('pic') 
        obj=pro_tbl.objects.create(uname=usn,email=eml,address=adrs,picture=pict)
        obj.save()
        if obj:
            return render(request,"viewpro.html")
        else:
            return render (request,"profile.html")
    else:
        return render (request,"profile.html")  

def view(request):
    usn = request.POST.get('un')    
    eml = request.POST.get('em')  
    adrs = request.POST.get('ads') 
    pict = request.POST.get('pic') 
    obj=pro_tbl.objects.filter(uname=usn,email=eml,address=adrs,picture=pict)
    obj=pro_tbl.objects.all()
    if obj:
        return render(request,"viewpro.html")


# def view(request):
#     obj=pro_tbl.objects.all()    
#     return render(request,"viewpro.html",{"view":obj})

# def pro(request):
#     obj=reg_tbl.objects.all()
#     return render(request,"profile.html",{"data":obj})   