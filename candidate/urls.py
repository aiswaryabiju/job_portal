from django.urls import path
from candidate import views


urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profile",views.CandidateProfileCreateView.as_view(),name="cand-profile"),
    path("viewprofile",views.CandidateProfileDetailView.as_view(),name="cand-viewprofile"),
    path("joblist",views.JobListView.as_view(),name="cand-joblist"),
    path("job/detail/<int:id>",views.CandidateJobDetailView.as_view(),name="cand-jobdetail"),
    path("application/add/<int:id>",views.apply_now,name="apply_now"),
    path("myapplications",views.MyApplicationView.as_view(),name="my-app"),
    path("acceptedapps",views.Accepted_Applications.as_view(),name="accepted_apps"),
    path("profile/signout",views.SignOut,name="signout"),
    path("profile/edit/<int:id>",views.ProfileEditView.as_view(),name="profile-edit")
]