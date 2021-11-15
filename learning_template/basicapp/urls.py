from basicapp import views
from django.conf.urls import url

app_name = 'basicapp'
urlpatterns=[
    url('^relative/$',views.relative,name='relative'),
    url('^other/$',views.other,name='other'),

]
