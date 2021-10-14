from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('info_list/<int:info_id>/', views.info_list, name='info_list'),
    path('edit_data/<int:data_id>/', views.edit_data, name='edit_data'),
    path('info_form/', views.info_form, name='info_form'),
    path('data_form/', views.data_form, name='data_form'),
    path('edit_info/<int:info_id>/', views.edit_info, name='edit_info'),
    path('delete/<int:data_id>/', views.delete, name='delete'),
    path('delete_info/<int:info_id>/', views.delete_info, name='delete_info'),
]
