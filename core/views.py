# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import MarkdownPage


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['urls'] = [page.slug for page in MarkdownPage.objects.all()]
        return self.render_to_response(context)


class CustomCreateView(CreateView):
    template_name = "create_view.html"
    model = MarkdownPage
    fields = ['slug',
              'markdownx_field1',
              'markdownx_field2',
              'markdownx_field3']
    success_url = '/'


class PagesList(ListView):
    model = MarkdownPage


class PagesDetail(DetailView):
    model = MarkdownPage

    def get_context_data(self, **kwargs):
        context = super(PagesDetail, self).get_context_data(**kwargs)
        return context
