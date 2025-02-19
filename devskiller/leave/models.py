from enum import IntEnum

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    language = models.CharField(max_length=3, default="en")

    class Meta:
        default_related_name = "org_user"


class LeaveRequestStatus(IntEnum):
    open = 0
    accepted = 1
    rejected = 2
    closed = 3


STATUSES = tuple((item.value, item.name) for item in list(LeaveRequestStatus))


class LeaveRequest(models.Model):
    start = models.DateField()
    end = models.DateField()
    request_by = models.ForeignKey(
        "leave.User", on_delete=models.CASCADE, related_name="days_off"
    )
    request_ts = models.DateTimeField()
    manager = models.ForeignKey(
        "leave.User", on_delete=models.CASCADE, related_name="requests"
    )
    status = models.PositiveSmallIntegerField(
        default=LeaveRequestStatus.open, choices=STATUSES
    )
    review_ts = models.DateTimeField(null=True, blank=True)
