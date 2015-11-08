from django.conf.urls import url
from django.views.generic import TemplateView
from market import views
from market.views import MainView

urlpatterns = [
    #url(r'^r/$', views.post_results, name='results'),
    url(r'^$', TemplateView.as_view(template_name='market/mock_page.html'),
    name='index'),
]