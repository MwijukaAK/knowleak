from django.urls import path
from .views import ProfileView, ReportView, NotificationView, DashboardView

urlpatterns = [
    path("reports/", ReportView.as_view(), name="report"),
    path("notifications/", NotificationView.as_view(), name="notification"),
    path("", DashboardView.as_view(), name="dashboard"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
]