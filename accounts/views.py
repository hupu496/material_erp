from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from masters.models import Category
from django.db.models import Sum, F
from materials.models import MaterialMaster, MaterialReceipt, MaterialRequisition, MaterialOutward
def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('dashboard')

    return render(request,'accounts/login.html')
def dashboard(request):
    total_categories = Category.objects.count()

    total_materials = MaterialMaster.objects.count()

    low_stock_items = MaterialMaster.objects.filter(
        quantity__lte=F('critical_qty')
    ).count()

    inventory_value = MaterialMaster.objects.aggregate(
        total=Sum(F('quantity') * F('rate'))
    )['total'] or 0

    print(Category.objects.all())

    context = { 
        'total_categories': total_categories,
        'total_materials': total_materials,
        'low_stock_items': low_stock_items,
        'inventory_value': round(inventory_value, 2),
    }

    return render(request, 'accounts/dashboard.html', context)
def logout_view(request):
    logout(request)
    return redirect('login')  # or your login page name