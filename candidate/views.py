from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from candidate.forms import CandidateProfileForm,CandidateProfileUpdateForm
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
from candidate.filters import JobFilter
from django.contrib.auth import authenticate,login,logout

# Create your views here.


class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"
    def get(self,request,*args,**kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,"cand-home.html",{"filter":filter})



class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CandidateProfileDetailView(TemplateView):
    template_name = "cand-myprofile.html"


class JobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "cand-joblist.html"
    paginate_by = 2


class CandidateJobDetailView(DetailView):
    model = Jobs
    template_name = "cand-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context["status"]=qs
        return context



def apply_now(request,*args,**kwargs):
    job_id=kwargs.get("id")
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")


class MyApplicationView(ListView):
    model = Applications
    template_name = "applied_jobs.html"
    context_object_name = "applyjobs"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user).order_by("-date")

class Accepted_Applications(ListView):
    model = Applications
    template_name = "accepted_apps.html"
    context_object_name = "application"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status="accepted").order_by("-date")


def SignOut(request):
    logout(request)
    return redirect("signin")


class ProfileEditView(UpdateView):
    model = CandidateProfile
    template_name = "profile_edit.html"
    pk_url_kwarg = "id"
    form_class = CandidateProfileUpdateForm
    success_url = reverse_lazy("cand-home")
