from django.shortcuts import render
from .forms import student
from .models import registration
# Create your views here.
def user(request):
    if request.method == 'POST':
        fm = student(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['NAME']
           fn=fm.cleaned_data['FATHERS_NAME']
           mn=fm.cleaned_data['MOTHERS_NAME']
           dob=fm.cleaned_data['DOB']
           em=fm.cleaned_data['EMAIL']
           cn=fm.cleaned_data['CONTACT']
           ad=fm.cleaned_data['ADDRESS']
           pn=fm.cleaned_data['PINCOAD']
           reg = registration( NAME=nm,FATHERS_NAME=fn,MOTHERS_NAME=mn,EMAIL=em,DOB=dob,CONTACT=cn,
                               ADDRESS=ad,PINCOAD=pn)
           
           reg.save()
           fm=student()
           return render(request,'form/form1.html')
        
    else:
     fm=student()
    return render (request,'form/form.html',{'form':fm})
