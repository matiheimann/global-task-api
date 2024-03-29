"""
URL configuration for global_task_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from global_task_api_app.views import PersonViewSet, OfficerViewSet, VehicleViewSet, LoginView, LogoutView, CreateInfractionView, GetInfractionsView

router = DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'officers', OfficerViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create_infraction', CreateInfractionView.as_view(), name='create_infraction'),
    path('get_infractions', GetInfractionsView.as_view(), name='get_infractions')
]
