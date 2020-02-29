from django.views.generic.base import TemplateView

class ThankYouPageView(TemplateView):
    template_name = 'thankyou.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

