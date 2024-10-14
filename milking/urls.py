from django.urls import path
from . import views

app_name = 'milking'

urlpatterns = [
    path('list/', views.milking_view, name='milking_list'),
    path('view/<int:pk>', views.MilkingDetail.as_view(), name='milking_detail'),
    path('create/', views.milking_create, name='milking_create'),
    path('edit/<int:pk>', views.milking_update, name='milking_edit'),
    path('delete/<int:pk>', views.milking_delete, name='milking_delete'),
]
