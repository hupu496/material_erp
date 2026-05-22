from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
from masters.models import Category, SubCategory, WorkSpots, UnitMaster,PartyMaster
from materials.models import MaterialMaster
import base64,csv
from django.core.files.base import ContentFile
from openpyxl import Workbook
from django.http import HttpResponse
from io import BytesIO

def report_dashboard(request):

    if request.method == "POST":
        report_type = request.POST.get('report_type')
        selected_type = request.POST.get('type')
        file_format = request.POST.get('format')

        # =========================
        # PARTY REPORT
        # =========================
        if report_type == "party":
            queryset = PartyMaster.objects.all()

            if selected_type:
                queryset = queryset.filter(type=selected_type)

            if file_format == "csv":
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="party_report.csv"'

                writer = csv.writer(response)
                writer.writerow(['ID', 'Name', 'Type'])

                for obj in queryset:
                    writer.writerow([obj.id, obj.name, obj.type])

                return response

            elif file_format == "xlsx":
                wb = Workbook()
                ws = wb.active
                ws.title = "Party Report"

                ws.append(['ID', 'Name', 'Type'])

                for obj in queryset:
                    ws.append([obj.id, obj.name, obj.type])

                response = HttpResponse(
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=party_report.xlsx'
                wb.save(response)

                return response


        # =========================
        # MATERIAL REPORT
        # =========================
        if report_type == "material":
            queryset = MaterialMaster.objects.select_related('category')
           
            if selected_type:
                queryset = queryset.filter(category__name=selected_type)

            if file_format == "csv":
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="material_report.csv"'

                writer = csv.writer(response)
                writer.writerow([
                    'ID', 'Category', 'Description', 'Quantity', 'Rate', 'Rack No'
                ])

                for obj in queryset:
                    writer.writerow([
                        obj.id,
                        obj.category.name,
                        obj.description,
                        obj.quantity,
                        obj.rate,
                        obj.rackno
                    ])

                return response

            elif file_format == "xlsx":
                wb = Workbook()
                ws = wb.active
                ws.title = "Material Report"

                ws.append([
                    'ID', 'Category', 'Description', 'Quantity', 'Rate', 'Rack No'
                ])

                for obj in queryset:
                    ws.append([
                        obj.id,
                        obj.category.name,
                        obj.description,
                        obj.quantity,
                        obj.rate,
                        obj.rackno
                    ])

                response = HttpResponse(
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=material_report.xlsx'
                wb.save(response)

                return response

    # =========================
    # GET REQUEST (FORM LOAD)
    # =========================
    party_types = PartyMaster.objects.values_list('type', flat=True).distinct().order_by('type')
    material_types = MaterialMaster.objects.values_list('category__name', flat=True).distinct().order_by('category__name')

    return render(request, 'reports/master_report.html', {
        'types': party_types,          # default
        'material_types': material_types
    })
def master_report(request):
    if request.method == "POST":
        report_type = request.POST.get('report_type')      # 'party' or 'material'
        master_type = request.POST.get('type')             # CML, ELECTRICAL, etc.

        if report_type == 'material':
            # Filter Material Master based on type (assuming you have a 'type' field or use category/subcategory)
            queryset = MaterialMaster.objects.select_related('category', 'sub_category').all()

            if master_type:
                # Adjust filter according to your model structure
                # Example: if you have a field called 'type' in MaterialMaster
                queryset = queryset.filter(category__name__iexact=master_type)

            filename = f"Material_Master_Report_{master_type or 'All'}_{datetime.now().strftime('%Y%m%d')}"
            return generate_report(queryset, 'material', filename, request.POST.get('format', 'xlsx'))

        elif report_type == 'party':
            # Add your PartyMaster model logic here
            # queryset = PartyMaster.objects.all()
            # ... filter logic ...
            pass

    # GET Request - Show Form
    types = PartyMaster.objects.filter('type')   # Your dropdown options
     
    return render(request, 'reports/master_report.html', {
        'types': types,
    })


def generate_report(queryset, report_for, filename, file_format='xlsx'):
    if file_format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

        writer = csv.writer(response)
        if report_for == 'material':
            writer.writerow(['ID', 'Description', 'Category', 'Sub Category', 'Rate', 'Quantity', 'Rack No', 'Total Stock'])

            for item in queryset:
                writer.writerow([
                    item.id,
                    item.description,
                    item.category.name if item.category else '',
                    item.sub_category.sub_category if item.sub_category else '',
                    item.rate,
                    item.quantity,
                    item.rackno,
                    item.total_stock if hasattr(item, 'total_stock') else ''
                ])

        return response

    else:  # Excel (.xlsx)
        wb = Workbook()
        ws = wb.active
        ws.title = "Master Report"

        # Header
        if report_for == 'material':
            headers = ['ID', 'Description', 'Category', 'Sub Category', 'Rate', 'Quantity', 'Rack No', 'Total Stock']
            ws.append(headers)

            for col in ws.iter_cols(min_row=1, max_row=1, min_col=1, max_col=len(headers)):
                for cell in col:
                    cell.font = Font(bold=True)
                    cell.alignment = Alignment(horizontal='center')

            for item in queryset:
                ws.append([
                    item.id,
                    item.description,
                    item.category.name if item.category else '',
                    getattr(item.sub_category, 'sub_category', ''),
                    item.rate,
                    item.quantity,
                    item.rackno,
                    getattr(item, 'total_stock', '')
                ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'
        wb.save(response)
        return response


def stock_summary(request):
    return render(request,'reports/stock_summary.html')


def returnable_report(request):
    return render(request,'reports/returnable_report.html')