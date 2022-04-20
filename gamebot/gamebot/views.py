from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'
