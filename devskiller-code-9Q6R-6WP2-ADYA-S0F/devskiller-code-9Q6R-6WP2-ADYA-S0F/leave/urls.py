from django.urls import path, re_path
from django.views.generic import RedirectView

from leave import views

app_name = "leave"

urlpatterns = [
    re_path(r"^$", RedirectView.as_view(url="leave/list")),
    re_path(r"^leave/list$", views.LeaveRequestList.as_view(), name="LeaveRequestList"),
    re_path(
        r"^leave/create$", views.LeaveRequestCreate.as_view(), name="LeaveRequestCreate"
    ),
    re_path(
        r"^leave/(?P<pk>[\d]+)/$",
        views.LeaveRequestDetail.as_view(),
        name="LeaveRequestDetail",
    ),
    re_path(
        r"^leave/(?P<pk>[\d]+)/update$",
        views.LeaveRequestUpdate.as_view(),
        name="LeaveRequestUpdate",
    ),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
]
