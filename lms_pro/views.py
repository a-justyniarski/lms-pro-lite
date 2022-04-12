from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from courses.models import Subject, Course


class HomeView(TemplateView):
    template_name = 'lms_pro/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['courses'] = Course.objects.all()
        ctx['subjects'] = Subject.objects.all()

        return ctx