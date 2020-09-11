from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from contacts.forms import ContactForm, SurveyResponseForm


class HomePageView(SuccessMessageMixin, CreateView):
    form_class = SurveyResponseForm
    template_name = 'pages/index.html'
    success_url = reverse_lazy('pages:index')
    success_message = 'Thank you for signing up! We will let you know when we officially launch!'


class RegisterPageView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('pages:register')
    success_message = 'Success! Your submission has been received! You will receive an email confirmation with additional information and steps.'
