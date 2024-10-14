from django.urls import path
from . import views

app_name = 'cows'

urlpatterns = [
    path('', views.cow_view, name='cow_list'),
    path('view/<int:pk>', views.CowDetail.as_view(), name='cow_detail'),
    path('new/', views.cow_create, name='cow_new'),
    path('edit/<int:pk>', views.cow_update, name='cow_edit'),
    path('delete/<int:pk>', views.cow_delete, name='cow_delete'),
]