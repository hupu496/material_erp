# middleware.py

from datetime import date, timedelta
from django.shortcuts import redirect
from .models import SystemSetting, SystemActivation

class ActivationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # allow admin & activation page
        if request.path.startswith('/admin/') or request.path.startswith('/activate/'):
            return self.get_response(request)

        activation = SystemActivation.objects.first()
        setting = SystemSetting.objects.first()

        # if not exists create default
        if not setting:
            setting = SystemSetting.objects.create()

        trial_end = setting.first_use_date + timedelta(days=30)
        today = date.today()

        # if already activated → allow
        if activation and activation.activated:
            return self.get_response(request)

        # if expired → force activation page
        if today > trial_end:
            return redirect('/activate/')

        return self.get_response(request)