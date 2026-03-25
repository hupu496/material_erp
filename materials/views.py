from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from datetime import date
from masters.models import Category, SubCategory, WorkSpots, UnitMaster
from .models import MaterialMaster,MaterialReceipt,MaterialRequisition,MaterialOutward
import base64
from django.core.files.base import ContentFile

def material_master(request, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(MaterialMaster, pk=pk)

    if request.method == "POST":
        photo = request.FILES.get('photo')
        captured_photo = request.POST.get('captured_photo')

        if not photo and captured_photo:
            format, imgstr = captured_photo.split(';base64,')
            ext = format.split('/')[-1]
            photo = ContentFile(base64.b64decode(imgstr), name='captured.' + ext)

        data = {
            'category_id': request.POST.get('category'),
            'sub_category_id': request.POST.get('subcategory'),
            'work_spots_id': request.POST.get('workspots'),
            'description': request.POST.get('description'),
            'units_id': request.POST.get('units'),
            'rate': request.POST.get('rate'),
            'quantity': request.POST.get('quantity'),
            'rackno': request.POST.get('rackno'),
            'qty': request.POST.get('qty'),
            'critical_qty': request.POST.get('critical_qty'),
        }

        if instance:  # Update
            for key, value in data.items():
                setattr(instance, key, value)
            if photo:
                instance.photo = photo
            instance.save()
        else:  # Create
            MaterialMaster.objects.create(**data, photo=photo)

        return redirect('material_master')

    # GET request
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    workspots = WorkSpots.objects.all()
    units = UnitMaster.objects.all()

    data = MaterialMaster.objects.select_related(
        'category', 'sub_category', 'work_spots', 'units'
    ).all()

    return render(request, 'materials/material_master.html', {
        'category': category,
        'subcategory': subcategory,
        'workspots': workspots,
        'units': units,
        'data': data,
        'instance': instance,
        'is_edit': bool(instance),
    })


# ====================== DELETE VIEW ======================
def material_delete(request, pk):
    material = get_object_or_404(MaterialMaster, pk=pk)
    if request.method == "POST":
        material.delete()
        return redirect('material_master')
    return redirect('material_master')
def load_subcategory(request):

    category_id = request.GET.get('category')

    subcategory = SubCategory.objects.filter(
        category_id=category_id
    ).values('id','sub_category')

    return JsonResponse(list(subcategory), safe=False)
def material_receipt(request, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(MaterialReceipt, pk=pk)

    if request.method == "POST":
        try:
            totalno = int(request.POST.get('totalno') or 0)
            rate = float(request.POST.get('rate') or 0)
            total_stock = float(request.POST.get('total_stock') or 0)

            data = {
                'issue_date': request.POST.get('issue_date'),
                'entry_no': int(request.POST.get('entry_no') or 0),
                'challan_no': request.POST.get('challan_no') or '',
                'category_id': request.POST.get('category'),
                'sub_category_id': request.POST.get('subcategory'),
                'item_id': request.POST.get('item'),
                'totalno': totalno,
                'rate': rate,
                'rackno': request.POST.get('rackno') or '',
                'total_stock': int(total_stock),           # Change to DecimalField later if needed
                'receive_from': request.POST.get('receive_from') or '',
                'vehicle_no': request.POST.get('vehicle_no') or '',
                'receiver': request.POST.get('receiver') or '',
                'remarks': request.POST.get('remarks') or '',
            }

            if instance:  # Edit
                for key, value in data.items():
                    setattr(instance, key, value)
                instance.save()
            else:  # Create
                MaterialReceipt.objects.create(**data)

            return redirect('material_receipt')

        except Exception as e:
            print("Error saving receipt:", e)

    # GET - Show form + list
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    materials = MaterialMaster.objects.select_related('category').all()

    receipts = MaterialReceipt.objects.select_related(
        'category', 'sub_category', 'item'
    ).order_by('-issue_date')

    return render(request, 'materials/material_receipt.html', {
        'categories': categories,
        'subcategories': subcategories,
        'materials': materials,
        'receipts': receipts,
        'instance': instance,
        'is_edit': bool(instance),
        'today': date.today(),
    })


# ====================== DELETE VIEW ======================
def material_receipt_delete(request, pk):
    receipt = get_object_or_404(MaterialReceipt, pk=pk)
    if request.method == "POST":
        receipt.delete()
    return redirect('material_receipt')


def material_requisition(request, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(MaterialRequisition, pk=pk)

    if request.method == "POST":
        try:
            data = {
                'issue_date': request.POST.get('issue_date'),
                'entry_no': int(request.POST.get('entry_no') or 0),
                'requisition_no': request.POST.get('requisition_no') or '',
                'category_id': request.POST.get('category'),
                'sub_category_id': request.POST.get('subcategory'),
                'work_spots_id': request.POST.get('work_spots'),
                'item_id': request.POST.get('item'),
                'total_nos': int(request.POST.get('total_nos') or 0),
                'requisition_by': request.POST.get('requisition_by') or '',
                'remarks': request.POST.get('remarks') or '',
            }

            if instance:  # Edit Mode
                for key, value in data.items():
                    setattr(instance, key, value)
                instance.save()
            else:  # Create Mode
                MaterialRequisition.objects.create(**data)

            return redirect('material_requisition')

        except Exception as e:
            print("Error in requisition:", e)

    # GET Request
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    workspots = WorkSpots.objects.all()
    materials = MaterialMaster.objects.select_related('category').all()

    # Get all requisitions for listing
    requisitions = MaterialRequisition.objects.select_related(
        'category', 'sub_category', 'work_spots', 'item'
    ).order_by('-issue_date')

    return render(request, 'materials/material_requisition.html', {
        'categories': categories,
        'subcategories': subcategories,
        'workspots': workspots,
        'materials': materials,
        'requisitions': requisitions,
        'instance': instance,
        'is_edit': bool(instance),
        'today': date.today(),
    })


# ====================== DELETE VIEW ======================
def material_requisition_delete(request, pk):
    requisition = get_object_or_404(MaterialRequisition, pk=pk)
    if request.method == "POST":
        requisition.delete()
    return redirect('material_requisition')


def material_outward(request, pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(MaterialOutward, pk=pk)

    if request.method == "POST":
        try:
            data = {
                'issue_date': request.POST.get('issue_date'),
                'entry_no': int(request.POST.get('entry_no') or 0),
                'location': request.POST.get('location') or '',
                'contents': request.POST.get('contents') or '',
                'contents2': request.POST.get('contents2') or '',
                'description': request.POST.get('description') or '',
                'totalno': int(request.POST.get('totalno') or 0),
                'vendor': request.POST.get('vendor') or '',
                'issuedto': request.POST.get('issuedto') or '',
                'vehicleno': request.POST.get('vehicleno') or '',
                'purpose': request.POST.get('purpose') or '',
                'issuer': request.POST.get('issuer') or '',
                'returnable': bool(request.POST.get('returnable')),
                'remarks': request.POST.get('remarks') or '',
                'acknowledgement': bool(request.POST.get('acknowledgement')),
            }

            if instance:  # Edit Mode
                for key, value in data.items():
                    setattr(instance, key, value)
                instance.save()
            else:  # Create Mode
                MaterialOutward.objects.create(**data)

            return redirect('material_outward')

        except Exception as e:
            print("Outward Error:", e)

    # GET Request - Form + List
    outward_list = MaterialOutward.objects.order_by('-issue_date')

    return render(request, 'materials/material_outward.html', {
        'outward_list': outward_list,
        'instance': instance,
        'is_edit': bool(instance),
        'today': date.today(),
    })


# AJAX: Fetch data from MaterialReceipt using entry_no
def fetch_receipt_by_entry(request):
    entry_no = request.GET.get('entry_no')
    if not entry_no:
        return JsonResponse({'error': 'No entry_no provided'}, status=400)

    try:
        receipt = MaterialReceipt.objects.get(entry_no=entry_no)
        data = {
            'success': True,
            'totalno': receipt.totalno,
            'description': receipt.item.description if receipt.item else '',
            'category': receipt.category.name if receipt.category else '',
            'sub_category': receipt.sub_category.sub_category if receipt.sub_category else '',
            'rate': receipt.rate,
            'rackno': receipt.rackno,
        }
        return JsonResponse(data)
    except MaterialReceipt.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'No receipt found with this Entry No'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


# Delete View
def material_outward_delete(request, pk):
    outward = get_object_or_404(MaterialOutward, pk=pk)
    if request.method == "POST":
        outward.delete()
    return redirect('material_outward')