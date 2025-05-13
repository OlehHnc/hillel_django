from first_app.models import Position, Department
from django.db.models import Q
from django.shortcuts import render
from first_app.models import Position


def query_departments_with_managers(request):
    departments = Department.objects.filter(position__is_manager=True).order_by("name").distinct()
    return render(request, "departments.html", {"departments": departments})


def all_activ_positions(request):
    positions_activ = Position.objects.filter(is_active=True).count()
    return render(request, "positions_activ.html", {"positions_activ": positions_activ})


def all_activ_or_hr_positions(request):
    positions_activ_or_hr = Position.objects.filter(
        Q(is_active=True) |
        Q(department__name__icontains='HR')
    ).order_by("title").distinct()
    return render(request, "positions_activ_or_hr.html", {"positions": positions_activ_or_hr})


def name_departments_with_managers(request):
    departments_with_managers = Department.objects.filter(position__is_manager=True).values("name").distinct()
    return render(request, "departments_with_managers.html", {"departments": departments_with_managers})


def all_positions(request):
    positions_all = Position.objects.all().order_by("title").values("title", "is_active")
    return render(request, "positions_list.html", {"positions": positions_all})