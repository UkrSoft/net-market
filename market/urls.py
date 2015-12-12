from django.conf.urls import url
from django.views.generic import TemplateView
from market import views
from market.views import MainView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='market/index.html'), name='index'),
    url(r'^shops/$', views.shops, name='shops'),
    url(r'^shops/(?P<item_id>\d+)/$', views.shops, name='shops_one'),
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^goods/(?P<item_id>\d+)/$', views.goods, name='goods_one'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^pass_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
]