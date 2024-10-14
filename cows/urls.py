from django.urls import path
from . import views

app_name = 'cows'

urlpatterns = [
    path('list/', views.cow_view, name='cow_list'),
    path('view/<int:pk>', views.CowDetail.as_view(), name='cow_detail'),
    path('create/', views.cow_create, name='cow_create'),
    path('edit/<int:pk>', views.cow_update, name='cow_edit'),
    path('delete/<int:pk>', views.cow_delete, name='cow_delete'),
]
