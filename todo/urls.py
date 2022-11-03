from django.urls import path

from todo import views
from todo.views import viewf

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('viewf',views.viewf,name='viewf'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]