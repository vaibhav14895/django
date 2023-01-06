from django.shortcuts import render,redirect
from django.http import HttpResponse
from services.models import service
# from .forms import usersForm
# Create your views here.


def index(request):
    return HttpResponse("hello vaibhav")


def dynamic(request, dynamic):
    return HttpResponse(dynamic)


def home(request):  
    return render(request, "index.html")

def blog(request):
    blogdata = service.objects.all()
    data={
        'sd':blogdata
    }
    return render(request,"blog.html",data)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request,"contact.html") 
        

def userform(request):
        try:
         if request.method=="post":
            n1=request.POST.get('NAME')
            n2=request.POST.get('GMAIL')
            n3=request.POST.get('NUMBER')
            n4=request.POST.get('MESSAGE')
            print(n1+n2+n3+n4)
        except:
            pass
        return render(request,"index.html")

   
def calc(request):
    c = ''
    if request.method == "POST":
        if request.POST.get('num1') == "" or request.POST.get('num2') == "":
            return render(request,"calc.html",{'error':True})
    
    if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
             c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2

            else:
                 c = "invalid operation"
    print(c)
    return render(request ,"calc.html",{'c':c})