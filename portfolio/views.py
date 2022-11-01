from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.views import generic
from . forms import ContactForm

def home(request):
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'skills': skills,
        'certificates': certificates
    }
    return render(request,
                  template_name='index.html', context=context)

def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request,
                  template_name='portfolio.html', context=context)


class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)