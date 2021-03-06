"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers

from carrier.views import CarrierView, FreightPriceView, PriceCalculatedView, CarrierPricesImportView
from origindestiny.views import OriginDestinyView
from weight.views import WeightView

router = routers.DefaultRouter()
router.register(r'carrier', CarrierView, basename='carrier')
router.register(r'origindestiny', OriginDestinyView, basename='origindestiny')
router.register(r'freight-price', FreightPriceView, basename='freight')
router.register(r'calculator', PriceCalculatedView, basename='calculator')
router.register(r'weight', WeightView, basename='weight')
# router.register(r'carrier-import', CarrierPricesImportView, basename='carrier-import')

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST API root view (generated by DRF router)
    path('', include(router.urls)),
    path('prices-import', CarrierPricesImportView.as_view(), name="prices-import")
]
