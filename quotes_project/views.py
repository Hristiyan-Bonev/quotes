from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Category, Author, Quote
import random



class IndexView(TemplateView):

    template_name = 'index.html'
    model = Quote

    def get_context_data(self, **kwargs):

        categories = Category.objects.all().order_by('category_text')
        quotes = Quote.objects.all().order_by('category')
        carousel_quotes = [random.choice(quotes) for _ in range(3)]
        carousel_images = [random.randint(1, 12) for _ in range(3)]
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        context['carousel_data'] = zip(carousel_quotes, carousel_images)
        return context


class CategoryView(ListView):
    model = Category
    template_name = 'category_view.html'

    def get_queryset(self):
        self.category_id = Category.objects.filter(category_text=self.kwargs['category']).values('category_id')
        self.category_quotes = Quote.objects.all() # FILTER
        self.category = Category.objects.filter(category=self.kwargs['category'])
        return self.category_quotes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = self.category_quotes[:55]
        context['category'] = self.category
        context['image_no'] = [random.randint(1,10) for _ in range(len(context['quotes']))]
        return context


class CategoriesList(ListView):
    model=Category
    template_name='category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories[:1204]
        context['categories_count'] = len(context['categories'])
        return context

class AuthorsList(ListView):
    model=Author
    template_name = 'authors_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.filter(author_id__lt='1000')
        char_list = list(set([x.author[0] for x in authors]))
        # Set of alphanumeric chars only
        unique_chars = set([char.lower() for char in char_list if ord(char) < 128])
        # Get only alphabet letters
        unique_chars = sorted([char for char in unique_chars if char.isalpha()])
        sorted_authors={}

        for char in unique_chars:
            # Create dictionary with first letter as key and corresponding
            # authors with first letter matching as values
            sorted_authors[char] = sorted([(x.author.strip(), x.author_id)  \
                                           for x in authors \
                                           if x.author[0].lower() == char \
                                           and len(x.author) < 15])

        context['authors'] = sorted_authors
        context['authors_count'] = len(authors)
        return context


class AuthorDetails(DetailView):
    model=Author
    template_name = 'author_details.html'
    paginate_by = 5
    count = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.author = Author.objects.filter(author_id=self.kwargs['pk'])
        self.author_quotes = Quote.objects.filter(author__author_id__contains=self.kwargs['pk'])
        context['author'] = self.author
        context['author_quotes'] = self.author_quotes[count:count + 50] # 0 - 50
        # count += 50
        # if request == 'GET':
        #     self.get_more()
        return context
    #
    # def get_more(self, request):
    #     try:
    #         context['author_quotes'] = self.author_quotes[count:count + 50] # 50-100
    #     except IndexError:
    #         context['']

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'sign_up.html'
