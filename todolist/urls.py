from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskCreateView, TaskDetailsView,\
                   TasklistCreateView, TasklistDetailsView,\
                   UserCreateView, UserDetailsView

urlpatterns = {
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$',
        TasklistDetailsView.as_view(),
        name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/$',
        TaskCreateView.as_view(),
        name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)/$',
        TaskDetailsView.as_view(),
        name="task-detail"),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^users/$', UserCreateView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(),
        name="user-detail")
}

urlpatterns = format_suffix_patterns(urlpatterns)
