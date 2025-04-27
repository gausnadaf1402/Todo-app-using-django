from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('todo/',views.todo,name='todo'),
    path('edit_todo/<int:sr_no>/',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:sr_no>/',views.delete_todo,name='delete_todo'),
    path('signout',views.signout,name="signout")
]
