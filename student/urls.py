from django.urls import path
from . import views
from student.views import*

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('add_stu/', views.add_stu, name='add_stu'),

    path('About/', views.About, name='About'),
    path('show_contact/', views.show_contact, name='show_contact'),

    path('add_stu1/', views.add_stu1, name='add_stu1'),

    path('masterDashboard/', views.masterDashboard, name='masterDashboard'),
    path('add_stu_save/', views.add_stu_save, name='add_stu_save'),

    path('add_stu1_save/', views.add_stu1_save, name='add_stu1_save'),

    path('edit_stu/^(?P<stu_id>\w+)/$', views.edit_stu, name='edit_stu'),
    path('stu_edit_save/^(?P<stu_id>\w+)/$', views.stu_edit_save, name='stu_edit_save'),
    path('del_stu/^(?P<stu_id>\w+)/$', views.del_stu, name='del_stu'),
    path('download/', views.download, name='download'),

]