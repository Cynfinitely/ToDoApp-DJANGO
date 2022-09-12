from django.urls import path
from .views import home, todo_create, todo_list, todo_update, todo_delete

urlpatterns = [
    path("", home, name="home"),
    path("list/", todo_list, name="todo-list"),
    path('create/',todo_create, name="todo-create"),
    path('update/<int:id>/', todo_update, name="todo-update"),
    path('delete/<int:id>/', todo_delete, name='todo-delete'),
]