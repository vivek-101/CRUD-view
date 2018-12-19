from django.conf.urls import url
from first import views

app_name = 'first'

urlpatterns = [
    url(r'^$',views.School_Listview.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.School_detailview.as_view(),name='detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),

]
