# Create your views here.
from django.views.generic import TemplateView, CreateView
from .models import MyModel


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class TestCreateView(CreateView):
    template_name = "test_create_view.html"
    model = MyModel
    fields = ['markdownx_field1', 'markdownx_field2', 'markdownx_field3']
    success_url = '/'