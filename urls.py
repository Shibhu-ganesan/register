from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('startup/', views.startup_page, name="startup"),
    path('login/', views.l_login, name="login"),
    path('register/',views.reg_before,name='reg_before'),
    path('member/', views.member_page, name="member"),
    path('investor', views.investor_page, name="investor"),
    path('startup/startup_form', views.startup_form, name="startup_form"),
    path('member/member_form', views.member_form, name="member_form"),
    path('investor/investor_form', views.investor_form, name="investor_form"),
    path('member_register/', views.member_register, name='mem_reg'),
    path('investor_register/', views.investor_register, name='inv_reg'),
    path('startup_register/', views.startup_register, name='sta_reg'),
]
