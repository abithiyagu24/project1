# from django.db import router
from django.urls import path, include
from djangoapi1 import views

urlpatterns = [
    # path('api/', include(router.urls)),
    path('department/', views.department),  ##Api for department create and list views get.
    path('department/<str:pk>/', views.departmentcurdapi),  ##Api for PUT, PATCH and GET a paticular data.
    path('empolyees/', views.employee),  ##Api for department create and list views get.
    path('empolyees/<str:pk>/', views.employeecurdapi)  ##Api for PUT, PATCH and GET a paticular data.

]
