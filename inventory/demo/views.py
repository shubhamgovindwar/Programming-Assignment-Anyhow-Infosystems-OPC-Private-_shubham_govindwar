from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required




def add_inventory(request):
    form=AddInventoryForm()
    if request.method=='POST':
        obj=AddInventoryForm(request.post)
        if obj.is_valid():
            obj.save()

        return redirect('/add_inventory.html/')
    return render(request,'demo/add_inventory.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('demo/add_inventory.html/')
    else:
        form = SignUpForm()
        return render(request, 'demo/signup.html', {'form': form})


# @login_required
def fetch_pending_inventory(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.roles.filter(name='Store Manager').exists():
        pending_inventory = InventoryRecord.objects.filter(status='Pending')
    else:
        pending_inventory = InventoryRecord.objects.filter(status='Pending', requested_by=user_profile)
    
    context = {'pending_inventory': pending_inventory}
    return render(request, 'pending_inventory.html', context)

# @login_required
def approve_inventory(request, inventory_id):
    user_profile = UserProfile.objects.get(user=request.user)
    inventory = get_object_or_404(InventoryRecord, pk=inventory_id, status='Pending')
    
    if user_profile.roles.filter(name='Store Manager').exists():
        inventory.status = 'Approved'
        inventory.approved_by = user_profile
        inventory.save()
        return redirect('demo/fetch_pending_inventory')
    else:
        return render(request, 'demo/error.html', {'message': 'You do not have permission to approve this record.'})
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_inventory')  # Redirect to the dashboard after successful login
        else:
            return render(request, 'demo/login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'demo/login.html')