from django.urls import path, include
from companyappapi.views import CompanyView, EmployeeView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies', CompanyView)
router.register(r'employees', EmployeeView)

urlpatterns = [
    path('', include(router.urls))
]