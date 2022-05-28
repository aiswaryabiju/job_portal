from django import forms
from candidate.models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=("user",)


class CandidateProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=("user",)