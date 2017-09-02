from django.conf.urls import url
from . import views

app_name = 'department_view'

urlpatterns = [
    #For Individual Departments of the Hospital
    # /find_student/
    url(r'^/$', views.show_dept_details, name='show_dept_details'),
]