from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    html="Please <a href=getData>Introduce Yourself</a>"
    return HttpResponse(html)

def showData(request):
    if request.method=='POST':
        value1=request.POST['fname']
        value2=request.POST['lname']
        name=value1+" "+value2
        return render(request,'showData.html',{'name':name})
    
def getData(request):
    return render(request,'getData.html')
