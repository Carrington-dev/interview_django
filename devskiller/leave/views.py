from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import redirect, resolve_url

from leave import models


class LeaveRequestList(ListView):
    template_name = "leave/LeaveRequest/list.html"
    model = models.LeaveRequest


class LeaveRequestCreate(LoginRequiredMixin, CreateView):
    template_name = "leave/LeaveRequest/form.html"
    model = models.LeaveRequest
    fields = ("start", "end")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # TODO: Setup user foreign keys from request here
        return form


class LeaveRequestDetail(LoginRequiredMixin, DetailView):
    template_name = "leave/LeaveRequest/detail.html"
    model = models.LeaveRequest

    def post(self, request, *args, **kwargs):
        leave_request = self.get_object()
        return redirect(resolve_url("leave:LeaveRequestList"))


class LeaveRequestUpdate(UserPassesTestMixin, UpdateView):
    template_name = "leave/LeaveRequest/form.html"
    model = models.LeaveRequest
    fields = ("start", "end")

