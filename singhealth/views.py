from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import Complaint_Form, Update_Form, Complaint_Tenant, Complaint_Notes
from .models import Complaint, Tenant, Staff, Outlet, Update
from django.utils import timezone

from .serializer import ComplaintSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import  CreateUserForm

from .decorators import *

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def create_complaint(request):
    context = {}

    context['staff'] = request.user
            
    form1 = Complaint_Tenant()
    context['form_complaint1'] = form1
    form2 = Update_Form()
    context['form_update'] = form2    
    form3 = Complaint_Form()
    context['form_complaint2'] = form3
    
    if request.method == 'POST':
       
        form1 = Complaint_Tenant(request.POST, request.FILES)
        form2 = Complaint_Form(request.POST, request.FILES)
        form3 = Update_Form(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            complaint = form2.save(commit=False)
            #complaint1 = form1.save(commit=False)
            complaint1 = form1.cleaned_data['tenant']
            complaint.tenant = complaint1
            complaint.status = 'Open'
            #staffUsername = request.POST.get('userId', -1)
            complaint.staff = request.user
            if form3.is_valid():
                update = form3.save(commit=False)
                update.complaint = complaint
                update.edit_name = str(complaint.staff.username)
                complaint.subject = update.subject
                complaint.save()
                update.save() 
                
                return redirect('homestaff')
    return render(request, 'create.html', context)


        
    

# def create_success(request):
#     context = {}
#     complaint = Complaint.objects.last()
#     context['complaint'] = complaint
#     update = Update.objects.get(complaint = complaint)
#     context['update'] = update
#     return render(request, 'complaint_success.html', context)

# def login(request):
#     return render(request, 'login_buttons.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def homestaff(request):
    context = {}
    
    # loginId = request.POST.get('loginId', -1)
    # staff = Staff.objects.get(username = loginId)
        
    # context['staff'] = staff    
    # tenants = Tenant.objects.all()
    # context['tenants'] = tenants
    # complaints = Complaint.objects.filter(staff = staff).order_by('date_created')[::-1]
    # context['complaints'] = complaints

    username = request.user.username
    #tenants = Tenant.objects.all()
    User = get_user_model()
    #users = User.objects.all()
    tenants = User.objects.filter(groups__name='Tenant')
    complaints = Complaint.objects.all()

    context['staff'] = username
    context['tenants'] = tenants
    context['complaints'] = complaints

    
    return render(request, 'home_staff.html', context)    
    
    
    
    
def hometenant(request):
    context = {}
    if request.method == 'POST':
        
        loginId = request.POST.get('loginId', 0)
        tenant = Tenant.objects.get(username = loginId)
        context['tenant'] = tenant
        complaints = Complaint.objects.filter(tenant = tenant).order_by('date_created')[::-1]
        context['complaints'] = complaints
        return render(request, 'home_tenant.html', context)    
    
    return render(request, 'error.html')




def view_tenant(request):
    if request.method == "POST":
        context = {}
        # tenantId = request.POST.get('tenantId', -1)
        # staffId = request.POST.get('staffId', -1)
        # tenant = Tenant.objects.get(username = tenantId)
        # staff = Staff.objects.get(username = staffId)
        # complaints = Complaint.objects.filter(staff = staff, tenant = tenant).order_by('date_created')[::-1]

        username = request.user.username
        #tenants = Tenant.objects.all()
        User = get_user_model()
        #users = User.objects.all()

        #get username of tenant
        tenantId = request.POST.get('tenantId', -1)
        tenant = User.objects.get(username=tenantId)

        #to channge to filter out complaint against specific tenant
        complaints = Complaint.objects.all()

        context['tenant'] = tenant
        context['complaints'] = complaints
        context['staff'] = staff
        return render(request, 'view_tenant.html', context)
        
    

def view_complaint(request):
    if request.method == "POST":
        context = {}
        
        
        try:
            complaintId = request.POST.get('complaintId', -1)
            complaint = Complaint.objects.get(id = complaintId)
            identity = request.POST.get('identity', 0)
            if identity == "staff":
                action = "Upload more details"
            elif identity == "tenant":
                action = "Upload Rectification"            
            context['action'] = action
            
       
        except:
            
            complaintid = request.POST.get('resolveid', -1)
            complaint = Complaint.objects.get(id = complaintid)  
            complaint.status = 'Resolved' 
            complaint.save()
            identity = "staff"
            
        
        updates = Update.objects.filter(complaint = complaint)
        context['updates'] = updates
        context['complaint'] = complaint
        context['identity'] = identity
        return render(request, 'view_complaint.html', context)
            
        
    return render(request, 'error.html')

def update(request):
    if request.method == "POST":
        context = {}
        identity = request.POST.get('identity', 0)
        complaintId = request.POST.get('updateid', -1)
        complaint = Complaint.objects.get(id = complaintId)
        form1 = Update_Form()
        updates = Update.objects.filter(complaint = complaint)
        
        
        if identity == "staff":
            form2 = Complaint_Notes()
            context['form_notes'] = form2
            title = "Update Complaint"
        
        elif identity == "tenant":
            title = "Upload Rectification"

        context['identity'] = identity
        context['complaint'] = complaint
        context['form_update'] = form1
        context['updates'] = updates
        context['title'] = title
        
            
        return render(request, 'update.html', context)
    
    return render(request, 'error.html')

def update_success(request):
    if request.method =="POST":
        complaintId = request.POST.get('comId', -1)
        complaint = Complaint.objects.get(id=complaintId)
        update = Update_Form(request.POST, request.FILES)
        if update.is_valid():
            u = update.save(commit = False)
            u.complaint = complaint
        else: 
            return render(request, 'error.html')
        
        identity = request.POST.get('identity', 0)
        
        
        if identity == "staff":
            action = "Update"
            userId = complaint.staff.username
            u.edit_name = complaint.staff.name
            u.save()
            notes = Complaint_Notes(request.POST, request.FILES)
            if notes.is_valid():
                n = notes.save(commit = False)
                complaint.notes += "\n" + n.notes
                complaint.save()
                return redirect('/singhealth/successstaff')
            
        elif identity == "tenant":
            action = "Rectification"
            userId = complaint.tenant.username
            u.edit_name = complaint.tenant.name
            u.save()
            return redirect('/singhealth/successtenant')
            
    
    return render(request, 'error.html')

def success_staff(request):
    context = {}
    update = Update.objects.order_by('date')[::-1][0]
    userId = update.complaint.staff.username
    context['userId'] = userId
    context['action'] = "Update"
    context['identity'] = "staff"
    return render(request, 'success.html', context)

def success_tenant(request):
    context = {}
    update = Update.objects.order_by('date')[::-1][0]
    userId = update.complaint.tenant.username
    context['userId'] = userId
    context['action'] = "Rectification"
    context['identity'] = "tenant"
    return render(request, 'success.html', context)
    





def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='tenant')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if user.groups.filter (name='Staff'):
				return redirect('homestaff')
			elif user.groups.filter (name='Tenant'):
				return redirect('tenant')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff'])
def staff(request):
	return render(request, 'staff.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Tenant'])
def tenant(request):
	return render(request, 'tenant.html')
