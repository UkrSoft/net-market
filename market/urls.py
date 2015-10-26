from django.conf.urls import url
from market import views
from market.views import MainView

urlpatterns = [
    #url(r'^r/$', views.post_results, name='results'),
    url(r'^$', MainView.as_view(), name='index'),
]