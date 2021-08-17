from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Postion',views.postionView)
router.register('company',views.companyView)
urlpatterns=[
    path('',include(router.urls)),
    path('api', views.ChartData.as_view()),
]