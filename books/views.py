from django.views.generic import ListView, DetailView
from .models import Comix, Category


class ComixListView(ListView):
    model = Comix
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ComixDetailView(DetailView):
    model = Comix
    template_name = 'books/books_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ComixFromCategory(ListView):
    model = Comix
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    category = None
    paginate_by = 5

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Comix.objects.filter(category__slug=self.category.slug)
        if not queryset:
            sub_cat = Category.objects.filter(parent=self.category)
            queryset = Comix.objects.filter(category__in=sub_cat)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Комиксы из категории: {self.category.title}'
        return context
