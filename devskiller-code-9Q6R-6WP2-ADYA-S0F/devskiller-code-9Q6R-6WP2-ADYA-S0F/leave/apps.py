from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LeaveConfig(AppConfig):
    name = "leave"
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = _("Django Leave Basic Test")
