from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from contacts.forms import TapTheTableForm, SurveyResponseForm


class HomePageView(SuccessMessageMixin, CreateView):
    form_class = SurveyResponseForm
    template_name = 'pages/index.html'
    success_url = reverse_lazy('pages:index')
    success_message = 'Thank you for signing up! We will let you know when we officially launch!'


class TapTheTablePageView(SuccessMessageMixin, CreateView):
    form_class = TapTheTableForm
    template_name = 'pages/tap_the_table.html'
    success_url = reverse_lazy('pages:tap_the_table')
    success_message = 'Success! Your submission has been received! You will receive an email confirmation with ' \
                      'additional information and steps. '
