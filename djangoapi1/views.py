# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from djangoapi1.serializers import *


# create your views here.

@api_view(['POST', 'GET'])
def department(request):
    if request.method == 'POST':
        # department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=request.data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)


@api_view(['PUT', 'PATCH', 'GET', 'DELETE'])
def departmentcurdapi(request, pk):
    if request.method == 'GET':
        departments = Departments.objects.filter(DepartmentId=pk)
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'PUT' or request.method =='PATCH':
        department = Departments.objects.get(DepartmentId=pk)
        department_serializer = DepartmentSerializer(instance=department, data=request.data)
        if department_serializer.is_valid(raise_exception=True):
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=pk)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@api_view(['POST', 'GET'])
def employee(request):
    if request.method == 'POST':
        employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


@api_view(['PUT', 'PATCH', 'GET', 'DELETE'])
def employeecurdapi(request, pk):
    if request.method == 'GET':
        employee = Employees.objects.filter(EmployeeId=pk)
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'PUT' or request.method =='PATCH':
        employee = Employees.objects.get(EmployeeId=pk)
        employee_serializer = EmployeeSerializer(instance=employee, data=request.data)
        if employee_serializer.is_valid(raise_exception=True):
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=pk)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


# @api_view(['POST', 'PUT', 'PATCH', 'GET', 'DELETE'])
# def departmentapi(request, pk):
#     if request.method == 'POST':
#         # department_data = JSONParser().parse(request)
#         department_serializer = DepartmentSerializer(data=request.data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Added Successfully!!", safe=False)
#         return JsonResponse("Failed to Add.", safe=False)
#     elif request.method == 'GET':
#         if pk != None:
#             departments = Departments.objects.filter(DepartmentId=pk)
#             departments_serializer = DepartmentSerializer(departments, many=True)
#         else:
#             departments = Departments.objects.all()
#             departments_serializer = DepartmentSerializer(departments, many=True)
#         return JsonResponse(departments_serializer.data, safe=False)

#     elif request.method == 'GET':
#         departments = Departments.objects.filter(DepartmentId=pk)
#         departments_serializer = DepartmentSerializer(departments, many=True)
#         return JsonResponse(departments_serializer.data, safe=False)
#     elif request.method == 'PUT' or request.method =='PATCH':
#         department = Departments.objects.get(DepartmentId=pk)
#         department_serializer = DepartmentSerializer(instance=department, data=request.data)
#         if department_serializer.is_valid(raise_exception=True):
#             department_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)
#     elif request.method == 'DELETE':
#         department = Departments.objects.get(DepartmentId=pk)
#         department.delete()
#         return JsonResponse("Deleted Successfully!!", safe=False)