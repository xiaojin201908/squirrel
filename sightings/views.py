# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Sighting
from .forms import SightingForm
