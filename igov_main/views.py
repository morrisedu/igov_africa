from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
    title = "iGovAfrica - Innovation House"

    context = {
        "title": title,
    }

    return render(request, "index.html", context)