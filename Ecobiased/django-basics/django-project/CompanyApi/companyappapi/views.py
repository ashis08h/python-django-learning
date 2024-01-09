from django.shortcuts import render
from rest_framework import viewsets
from companyappapi.models import Company, Employee
from companyappapi.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companies_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        # detail=True, Whenever we add delete=True then only djangorestframework will allow
        # user to add company id in URL.
        print("get employees of ", pk, " Company.")
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"message": "Company does not Exists."})
        emps = Employee.objects.filter(company=company)
        emps_serializers = EmployeeSerializer(emps, many=True, context={'request': request})
        return Response(emps_serializers.data)


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer