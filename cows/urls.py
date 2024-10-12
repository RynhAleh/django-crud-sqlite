from django.urls import path
from . import views

app_name = 'cows'

urlpatterns = [
    path('', views.CowList.as_view(), name='cow_list'),
    path('view/<int:pk>', views.CowDetail.as_view(), name='cow_detail'),
    path('new/', views.CowCreate.as_view(), name='cow_new'),
    path('edit/<int:pk>', views.CowUpdate.as_view(), name='cow_edit'),
    path('delete/<int:pk>', views.CowDelete.as_view(), name='cow_delete'),
]