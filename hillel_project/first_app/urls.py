from django.urls import path

from first_app.views import func_views, generic_views, homework_querysets

urlpatterns = [
    # path('employees/', func_views.employee_list, name='employee_list'),
    path('employees/', generic_views.EmployeeListView.as_view(), name='employee_list'),
    # path('employees/update/<int:pk>/', func_views.employee_update, name='employee_update'),
    path('employees/update/<int:pk>/', generic_views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', func_views.employee_delete, name='employee_delete'),
    path('departments/', homework_querysets.query_departments_with_managers, name='departments'),
    path('positions_activ/', homework_querysets.all_activ_positions, name='positions_activ'),
    path('positions_activ_or_hr/', homework_querysets.all_activ_or_hr_positions, name='positions_activ_or_hr'),
    path('departments_with_managers/', homework_querysets.name_departments_with_managers, name='departments_with_managers'),
    path('positions_all/', homework_querysets.all_positions, name='positions_all'),

]