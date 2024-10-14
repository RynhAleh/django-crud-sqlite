from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('staff_list/', views.staff_view, name='staff_list'),
    path('staff_view/<int:pk>', views.StaffDetail.as_view(), name='staff_detail'),
    path('staff_create/', views.staff_create, name='staff_create'),
    path('staff_edit/<int:pk>', views.staff_update, name='staff_edit'),
    path('staff_delete/<int:pk>', views.staff_delete, name='staff_delete'),
]