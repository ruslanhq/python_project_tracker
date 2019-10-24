from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreate, TaskUpdate, TaskDelete, StatusView, TypeView,\
    StatusCreate, TypeCreate, StatusUpdate, TypeUpdate, StatusDelete, DeleteType, ProjectList, ProjectView,\
    ProjectCreate, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('status/list/', StatusView.as_view(), name='status_list'),
    path('type/list/', TypeView.as_view(), name='type_list'),
    path('status/create/', StatusCreate.as_view(), name='status_add'),
    path('type/create/', TypeCreate.as_view(), name='type_add'),
    path('status/update/<int:pk>/', StatusUpdate.as_view(), name='status_update'),
    path('type/update/<int:pk>/', TypeUpdate.as_view(), name='type_update'),
    path('status/delete/<int:pk>/', StatusDelete.as_view(), name='status_delete'),
    path('type/delete/<int:pk>/', DeleteType.as_view(), name='type_delete'),
    path('project/list/', ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdate.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete'),

]