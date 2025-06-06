# admin username ---> xyz
# admin password ---> xyz

from django.urls import path
from todolist import views
urlpatterns = [
    path("", views.home, name="home"),
    path("task", views.task, name="task"),
    path("saving-data", views.saveinfo, name="save"),
    path("delete-data/<int:xyz>", views.deletetask, name = "delete"),
    path("update-data/<int:myid>", views.updatetask, name = "update"),
    path("updated-data/<int:myid>", views.updating, name = "updated"),
    path("login", views.loginpage, name="login"),
    path("register", views.registerpage, name="register"),
    path("logout", views.logoutpage, name="logout"),
]