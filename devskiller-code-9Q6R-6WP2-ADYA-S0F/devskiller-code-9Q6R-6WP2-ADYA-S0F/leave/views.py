from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import redirect, render, resolve_url
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

from leave import models


class LeaveRequestList(LoginRequiredMixin, ListView):
    template_name = "leave/LeaveRequest/list.html"
    model = models.LeaveRequest
    paginator = Paginator
    paginate_by = 20


class LeaveRequestCreate( CreateView):
    template_name = "leave/LeaveRequest/form.html"
    model = models.LeaveRequest
    fields = ("start", "end")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.manager = self.request.user
        form.instance.request_by = self.request.user
        # TODO: Setup user foreign keys from request here
        return form
    
    def dispatch(self, request, *args, **kwargs):
        # object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("admin:index"))
        
        return render(request, "leave/LeaveRequest/form.html")

    def get_success_url(self):
        return reverse('leave:LeaveRequestDetail', kwargs={'pk': self.object.pk})

class LeaveRequestDetail(LoginRequiredMixin, DetailView):
    template_name = "leave/LeaveRequest/detail.html"
    model = models.LeaveRequest

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        leave_request = self.get_object()
        if leave_request.status == 1 or leave_request.status == 2:
            return redirect(resolve_url("leave:LeaveRequestList"))
        if leave_request.status in {0, 1}:
            return HttpResponseBadRequest('Please set correct status: {}'.format(request.method), \
                                      status=405)
        return HttpResponseForbidden()
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        object = self.get_object()
        # self.object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("leave:login"))
        if object.manager != request.user:
            raise PermissionDenied()
        context = super(LeaveRequestDetail, self).get_context_data(*args, **kwargs)
        return render(request, self.template_name, context)

class LeaveRequestUpdate(UserPassesTestMixin, UpdateView):
    template_name = "leave/LeaveRequest/form.html"
    model = models.LeaveRequest
    fields = ("start", "end")
    # authenticated_redirect_url = reverse_lazy(u"view_url")

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("leave:login"))
        if request.user.is_authenticated:
            return redirect("LeaveRequestDetail", pk=object.pk)
        if object.request_by != request.user:
            raise PermissionDenied()
        return render(request, "leave/LeaveRequest/form.html")



def login(request):
    return render(request, "auth/login.html")

def logout(request):
    return render(request, "auth/logout.html")

def register(request):
    return render(request, "auth/register.html")