from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistrationform
from .models import user
# Create your views here.

def addandshow(request):
    if request.method == 'POST':
        fm=studentregistrationform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pswrd=fm.cleaned_data['password']
            registration=user(name=nm,email=em,password=pswrd)
            registration.save()
            fm=studentregistrationform()
    else:
        fm=studentregistrationform()
    student=user.objects.all()
    return render(request,'addandshow.html',{'fm':fm,'stu':student})

def delete(request,id):
    if request.method == 'POST':
        p=user.objects.get(pk=id) #primary key
        p.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
        p=user.objects.get(pk=id) #primary key
        fm=studentregistrationform(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        p=user.objects.get(pk=id) #primary key
        fm=studentregistrationform(instance=p)
    return render(request,'updatestudent.html',{'form':fm})