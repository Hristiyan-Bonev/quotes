from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Categories, Authors, QuoteData


class IndexView(TemplateView):

    template_name = 'index.html'
    # model = Authors

    def get_context_data(self, **kwargs):
        categories = QuoteData.objects.all().order_by('category')[:55]
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        # import ipdb; ipdb.set_trace()
        return context
