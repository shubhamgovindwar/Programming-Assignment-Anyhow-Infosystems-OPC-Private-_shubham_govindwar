from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, InventoryRecord

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_inventory(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.roles.filter(name='Department Manager').exists():
        InventoryRecord.objects.create(
            product_id=request.data['product_id'],
            product_name=request.data['product_name'],
            vendor=request.data['vendor'],
            mrp=request.data['mrp'],
            batch_num=request.data['batch_num'],
            batch_date=request.data['batch_date'],
            quantity=request.data['quantity'],
            status='Pending',
            requested_by=user_profile
        )
        return Response({'message': 'Inventory record added and pending approval.'})
    else:
        InventoryRecord.objects.create(
            product_id=request.data['product_id'],
            product_name=request.data['product_name'],
            vendor=request.data['vendor'],
            mrp=request.data['mrp'],
            batch_num=request.data['batch_num'],
            batch_date=request.data['batch_date'],
            quantity=request.data['quantity'],
            status='Approved',
            requested_by=user_profile,
            approved_by=user_profile
        )
        return Response({'message': 'Inventory record added and auto-approved.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_pending_inventory(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.roles.filter(name='Store Manager').exists():
        pending_inventory = InventoryRecord.objects.filter(status='Pending')
    else:
        pending_inventory = InventoryRecord.objects.filter(status='Pending', requested_by=user_profile)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_inventory(request, inventory_id):
    user_profile = UserProfile.objects.get(user=request.user)
    inventory = InventoryRecord.objects.get(pk=inventory_id)
    
    if user_profile.roles.filter(name='Store Manager').exists() and inventory.status == 'Pending':
        inventory.status = 'Approved'
        inventory.approved_by = user_profile
        inventory.save()
        return Response({'message': 'Inventory record approved.'})
    else:
        return Response({'error': 'You do not have permission to approve this record.'})
