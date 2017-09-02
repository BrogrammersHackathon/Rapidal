from django.conf.urls import url
from . import views

app_name = 'hospital_dashboard'

urlpatterns = [
    # /

    # Page for Alumni to Find Students
    # /find_student/
    url(r'^find_student/$', views.find_student, name='find_student'),

]