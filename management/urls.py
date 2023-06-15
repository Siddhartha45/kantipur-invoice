from django.urls import path
from . import views


urlpatterns = [
    path('', views.Customer, name="index"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register',views.register,name='register'),
    path('reset',views.ResetPassword,name='reset'),
    path('delete/<int:id>/', views.Delete_table,name="delete_data"),
    path('edit/<int:id>/', views.update_data,name="update"),
    
    #path('',views.AddCustomer.as_view(),name='index')
]