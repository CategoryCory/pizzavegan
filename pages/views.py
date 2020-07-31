from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from contacts.forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'pages/index.html'


class RegisterPageView(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('pages:index')
    success_message = 'It worked!!'
