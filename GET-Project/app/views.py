from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html="please <a href=getData>Introduce yourself</a>"
    return HttpResponse(html)

def getData(request):
    return render(request,'getData.html')

def showResult(request):
    value1=request.GET['fname']
    value2=request.GET['lname']
    name=value1+" "+value2
    return render(request,'showResult.html',{'name':name})