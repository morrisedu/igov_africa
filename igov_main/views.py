from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests

from .functions import get_discontinued

# Create your views here.
def index(request):
    title = "iGovAfrica - Innovation House"

    data_2019 = get_discontinued("2019")["Results"]
    data_2020 = get_discontinued("2020")["Results"]

    in_2019 = len(data_2019)
    in_2020 = len(data_2020)

    context = {
        "title": title,
        "data_2019": data_2019,
        "2019_count": in_2019,
        "2020_count": in_2020,
        "data_2020": data_2020,
    }

    return render(request, "index.html", context)