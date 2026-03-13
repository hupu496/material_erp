from django.shortcuts import render


def report_dashboard(request):
    return render(request,'reports/dashboard.html')


def master_report(request):
    return render(request,'reports/master_report.html')


def stock_summary(request):
    return render(request,'reports/stock_summary.html')


def returnable_report(request):
    return render(request,'reports/returnable_report.html')