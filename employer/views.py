from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.forms import EmployerProfileForm,JobForm,JobUpdateForm
from employer.models import EmployerProfile,Jobs,Applications
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("ehome")


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"



class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("ehome")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,"Job has been posted successfully")
        return super().form_valid(form)


class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"


    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")


class EmployerJobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"



class EmployerJobUpdateView(UpdateView):
    model = Jobs
    template_name = "emp-jobupdate.html"
    form_class = JobUpdateForm
    success_url = reverse_lazy("ejoblist")
    pk_url_kwarg = "id"


class ViewApplications(ListView):
    model = Applications
    template_name = "all_applications.html"
    context_object_name = "all_apps"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"),status="applied")


class ApplicantDetailView(DetailView):
    model = Applications
    template_name = "applicant-detail.html"
    context_object_name = "applictns"
    pk_url_kwarg = "id"


def update_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    qs=Applications.objects.get(id=app_id)
    qs.status="rejected"
    qs.save()
    return redirect("ehome")




def accept_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    qs=Applications.objects.get(id=app_id)
    qs.status="accepted"
    qs.save()
    send_mail(
        "Job Notification",
        'You are accepted for participating the interview',
        'aiswaryabiju234@gmail.com',
        ['microsearch143@gmail.com'],
        fail_silently=False,
    )
    return redirect("ehome")


def signout(request):
    logout(request)
    return redirect("signin")


class EmpProfileUpdateView(UpdateView):
    model = EmployerProfile
    template_name = "emp-pro-edit.html"
    form_class = EmployerProfileForm
    success_url = reverse_lazy("ehome")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,"profile has been updated succesfully")
        return super().form_valid(form)



