"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreate, TaskUpdate, TaskDelete, status_view, type_view,\
    status_create, type_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('status/list/', status_view, name='status_list'),
    path('type/list/', type_view, name='type_list'),
    path('status/create/', status_create, name='status_add'),
    path('type/create/', type_create, name='type_add'),

]
