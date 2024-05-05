from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import user
from .forms import RegistrationUserForm
from resume.models import resume
from company.models import Company

# register applicant only
def register_applicant(request):
    if request.method=='POST':
        form= RegistrationUserForm(request.POST)
        if form.is_valid():
           var= form.save(commit=False)
           var.is_applicant= True
           var.username= var.email
           var.save()
           resume.objects.create(user=var)
           messages.info(request,'your account has been created.')
           return redirect('login')
        else:
            messages.warning(request,'something went wrong')
            return redirect('register-applicant')  
    else:
        form=RegistrationUserForm()
        context={'form':form}
        return render(request,'users/register_applicant.html',context)

# register recuiter only
def register_recuiter(request):
     if request.method=='POST':
        form= RegistrationUserForm(request.POST)
        if form.is_valid():
           var= form.save(commit=False)
           var.is_recuiter= True
           var.username= var.email
           var.save()
           Company.objects.create(user=var)
           messages.info(request,'your account has been created.')
           return redirect('login')
        else:
            messages.warning(request,'something went wrong')
            return redirect('register-recuiter')  
     else:
         form=RegistrationUserForm()
         context={'form':form}
         return render(request,'users/register_recuiter.html',context)
    

#login user
def login_user(request):
    if request.method=='POST':
        email= email.POST.get('email')
        password= password.POST.get('password')
        
        user= authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashbord')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('login')
    else:
        return render(request,'users/login.html' )
    
#logout user
def logout_user(request):
    logout(request)
    messages.info(request,'your session is ended')
    return redirect('login')
        
    