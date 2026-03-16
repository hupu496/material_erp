from django.shortcuts import render, redirect
from django.http import JsonResponse
from masters.models import Category, SubCategory, WorkSpots, UnitMaster
from .models import MaterialMaster


def material_master(request):

    if request.method == "POST":
       
        MaterialMaster.objects.create(
            category_id=request.POST.get('category'),
            sub_category_id=request.POST.get('subcategory'),
            work_spots_id=request.POST.get('workspots'),
            description=request.POST.get('description'),
            units_id=request.POST.get('units'),
            rate=request.POST.get('rate'),
            quantity=request.POST.get('quantity'),
            rackno=request.POST.get('rackno'),
            qty=request.POST.get('qty'),
            critical_qty=request.POST.get('critical_qty'),
            photo=request.FILES.get('photo')
        )

        return redirect('material_master')


    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    workspots = WorkSpots.objects.all()
    units = UnitMaster.objects.all()

    data = MaterialMaster.objects.select_related(
        'category','sub_category','work_spots','units'
    ).all()
    print(data)
    return render(request, 'materials/material_master.html', {
        'category': category,
        'subcategory': subcategory,
        'workspots': workspots,
        'units': units,
        'data': data
    })

def load_subcategory(request):

    category_id = request.GET.get('category')

    subcategory = SubCategory.objects.filter(
        category_id=category_id
    ).values('id','sub_category')

    return JsonResponse(list(subcategory), safe=False)
def material_receipt(request):
    return render(request, 'materials/material_receipt.html')


def material_requisition(request):
    return render(request, 'materials/material_requisition.html')


def material_outward(request):
    return render(request, 'materials/material_outward.html')