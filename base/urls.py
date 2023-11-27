from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('register/',views.register,name="register"),
    path('service/',views.service,name="services"),
    path('studentinfo/<str:param>/',views.studentinfo,name= "studentinfo"),
    path('viewall/', views.view_all, name="viewall")
]
