from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ViewProfileView(TemplateView):
    template_name = "profiles/view.html"
