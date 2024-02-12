from django.urls import path, include
from .. import views
from ..views import CustomLoginView
from ..views import user_logout, tasks_post,deleteTask,completed_tasks,uncompleted_tasks
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('completed_tasks/' , completed_tasks, name='completed_tasks'),
    path('uncompleted_tasks/' , uncompleted_tasks, name='uncompleted_tasks'),
    # path('login/' ,CustomLoginView.as_view(), name='login'),
    # path('logout/' ,views.user_logout, name='logout'),
    path('update_tasks/<int:id>/', views.updateTask, name="update_task"),
    path('delete/<int:id>/', deleteTask, name="delete"),
    path('post/', tasks_post, name = 'tasks_post' ),
]
