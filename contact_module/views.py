from django.views.generic.edit import CreateView
from site_module.models import SiteSetting
from .forms import ContactUsModelForm


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context
