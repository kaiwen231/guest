from django.conf.urls import url
from . import views_if

urlpatterns = [
    url(r'^add_event/', views_if.add_event,name='add_event'),
    url(r'^get_event_list/', views_if.get_event_list,name='get_event_list'),
    url(r'^add_guest/', views_if.add_guest,name='add_guest'),
    url(r'^get_guest_list/', views_if.get_guest_list,name='get_guest_list'),
    url(r'^guest_sign/', views_if.guest_sign,name='guest_sign'),
    # url(r'^index/$',views.index),
    # url(r'^login_action/$',views.login_action),
    # url(r'^event_manage/$',views.event_manage),
    # url(r'^event_search_name/$',views.event_search_name),
    # url(r'^guest_manage/$',views.guest_manage),
    # url(r'^guest_search_name/$',views.guest_search_name),
    # url(r'^sign_index/(?P<eid>[0-9]+)/$',views.sign_index),
    # url(r'^sign_index_action/(?P<eid>[0-9]+)/$',views.sign_index_action),
    # url(r'^logout/$',views.logout),
]
