
from django.urls import path
from.import views
app_name='todo_app1'

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('cbv/',views.task_list_view.as_view(),name='cbv'),
    path('cbv_detail/<int:pk>/',views.task_detail_view.as_view(),name='cbv_detail'),
    path('cbv_update/<int:pk>/',views.task_update_view.as_view(),name='cbv_update'),
    path('cbv_delete/<int:pk>/',views.task_delete_view.as_view(),name='cbv_delete'),
]