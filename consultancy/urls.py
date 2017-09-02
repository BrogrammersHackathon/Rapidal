from django.conf.urls import url
from . import views

app_name = 'consultancy'

urlpatterns = [
    # /

    # Page for Alumni to Find Students
    # /find_student/
    url(r'^/$', views.find_student, name='find_student'),

]