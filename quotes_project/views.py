from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Categories, Authors, QuoteData
import random

class IndexView(TemplateView):

    template_name = 'index.html'
    # model = Authors

    def get_context_data(self, **kwargs):
        quotes = QuoteData.objects.all().order_by('category')[:55]
        carousel_quotes = [random.choice(quotes) for _ in range(3)]
        carousel_images = [random.randint(1, 12) for _ in range(3)]
        context = super().get_context_data(**kwargs)
        context['quotes'] = quotes
        context['carousel_data'] = zip(carousel_quotes, carousel_images)
        return context
