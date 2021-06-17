from django.http import HttpResponse
from django.shortcuts import render
from Profiles.models import Profile


def home(request):
    profiles = Profile.objects.all()
    return render(request, "home.html", {'profiles': profiles})
