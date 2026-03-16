from django.http import JsonResponse
from .models import *
from django.shortcuts import render,redirect,get_object_or_404

def subcategory(request):

    if request.method == "POST":

        category_id = request.POST.get('category')
        sub_category = request.POST.get('sub_category')

        SubCategory.objects.create(
            category_id=category_id,
            sub_category=sub_category
        )

        return redirect('/masters/subcategory/')

    data = SubCategory.objects.select_related('category').all()
    category = Category.objects.all()

    return render(request,'masters/subcategory.html',{
        'data':data,
        'category':category
    })


def subcategory_edit(request,id):

    sub = SubCategory.objects.get(id=id)

    if request.method == "POST":

        sub.category_id = request.POST.get('category')
        sub.sub_category = request.POST.get('sub_category')
        sub.save()

        return redirect('/masters/subcategory/')

    data = SubCategory.objects.select_related('category').all()
    category = Category.objects.all()

    return render(request,'masters/subcategory.html',{
        'edit':sub,
        'data':data,
        'category':category
    })


def subcategory_delete(request,id):

    SubCategory.objects.filter(id=id).delete()

    return redirect('/masters/subcategory/')


def load_subcategory(request,id):

    data = SubCategory.objects.filter(category_id=id)

    result = []

    for i in data:
        result.append({
            'id': i.id,
            'name': i.sub_category
        })

    return JsonResponse(result,safe=False)
def category(request):

    if request.method == "POST":

        name = request.POST.get('name')

        Category.objects.create(
            name=name
        )

        return redirect('category')

    data = Category.objects.all()

    return render(request,'masters/category.html',{
        'data':data
    })

def category_edit(request, id):

    cat = Category.objects.get(id=id)

    if request.method == "POST":
        cat.name = request.POST.get('name')
        cat.save()
        return redirect('/masters/category/')

    data = Category.objects.all()

    return render(request, 'masters/category.html', {
        'edit': cat,
        'data': data
    })


def category_delete(request, id):

    cat = Category.objects.get(id=id)
    cat.delete()

    return redirect('/masters/category/')
def unit_master(request):

    if request.method == "POST":
        name = request.POST.get('name')
        UnitMaster.objects.create(name=name)

        return redirect('/masters/unit/')

    data = UnitMaster.objects.all()

    return render(request,'masters/unit_master.html',{
        'data':data
    })


def unit_edit(request,id):

    unit = UnitMaster.objects.get(id=id)

    if request.method == "POST":

        unit.name = request.POST.get('name')
        unit.save()

        return redirect('/masters/unit/')

    data = UnitMaster.objects.all()

    return render(request,'masters/unit_master.html',{
        'edit':unit,
        'data':data
    })


def unit_delete(request,id):

    UnitMaster.objects.filter(id=id).delete()

    return redirect('/masters/unit/')

def seller_type(request):

    if request.method == "POST":

        type = request.POST.get('type')

        TypeOfSeller.objects.create(type=type)

        return redirect('/masters/seller-type/')

    data = TypeOfSeller.objects.all()

    return render(request,'masters/seller_type.html',{
        'data':data
    })


def seller_type_edit(request,id):

    seller = TypeOfSeller.objects.get(id=id)

    if request.method == "POST":

        seller.type = request.POST.get('type')
        seller.save()

        return redirect('/masters/seller-type/')

    data = TypeOfSeller.objects.all()

    return render(request,'masters/seller_type.html',{
        'edit':seller,
        'data':data
    })


def seller_type_delete(request,id):

    TypeOfSeller.objects.filter(id=id).delete()

    return redirect('/masters/seller-type/')
def work_spots(request):

    if request.method == "POST":

        name = request.POST.get('name')

        WorkSpots.objects.create(name=name)

        return redirect('/masters/work-spots/')

    data = WorkSpots.objects.all()
    for d in data:
        d.first_word = d.name.split(" ")[0]

    return render(request,'masters/work_spots.html',{
        'data':data
    })


def work_spots_edit(request,id):

    spot = WorkSpots.objects.get(id=id)

    if request.method == "POST":

        spot.name = request.POST.get('name')
        spot.save()

        return redirect('/masters/work-spots/')

    data = WorkSpots.objects.all()

    return render(request,'masters/work_spots.html',{
        'edit':spot,
        'data':data
    })


def work_spots_delete(request,id):

    WorkSpots.objects.filter(id=id).delete()

    return redirect('/masters/work-spots/')
def party_master(request):

    if request.method == "POST":

        PartyMaster.objects.create(
            category_id=request.POST.get('category'),
            type=request.POST.get('type'),
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email')
        )

        return redirect('/masters/party-master/')

    data = PartyMaster.objects.select_related('category').all()
    category = Category.objects.all()

    return render(request,'masters/party_master.html',{
        'data':data,
        'category':category
    })


def party_master_edit(request,id):

    party = PartyMaster.objects.get(id=id)

    if request.method == "POST":

        party.category_id = request.POST.get('category')
        party.type = request.POST.get('type')
        party.name = request.POST.get('name')
        party.address = request.POST.get('address')
        party.phone = request.POST.get('phone')
        party.email = request.POST.get('email')

        party.save()

        return redirect('/masters/party-master/')

    data = PartyMaster.objects.select_related('category').all()
    category = Category.objects.all()

    return render(request,'masters/party_master.html',{
        'edit':party,
        'data':data,
        'category':category
    })


def party_master_delete(request,id):

    PartyMaster.objects.filter(id=id).delete()

    return redirect('/masters/party-master/')