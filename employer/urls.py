from django.urls import path
from employer import views

urlpatterns=[
    path("ehome",views.EmployerHomeView.as_view(),name="ehome"),
    path("profile/add",views.EmployerProfileCreateView.as_view(),name="eprofile"),
    path("profile/view",views.ProfileDetailView.as_view(),name="eprofileview"),
    path("jobs/add",views.JobCreateView.as_view(),name="eaddjob"),
    path("jobs/list",views.EmployerJobListView.as_view(),name="ejoblist"),
    path("jobs/detail/<int:id>",views.EmployerJobDetailView.as_view(),name="ejobdetail"),
    path("update/<int:id>",views.EmployerJobUpdateView.as_view(),name="ejobupdate"),
    path("viewapplications/<int:id>",views.ViewApplications.as_view(),name="viewapps"),
    path("profileview/<int:id>",views.ApplicantDetailView.as_view(),name="applicantprofile"),
    path("updated_status/<int:id>",views.update_application,name="updated_status"),
    path("accepted_status/<int:id>",views.accept_application,name="accepted_status"),
    path("profile/signout",views.signout,name="signout"),
    path("profile/edit/<int:id>",views.EmpProfileUpdateView.as_view(),name="emp-pro-edit")

]