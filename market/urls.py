from django.conf.urls import url
from django.views.generic import TemplateView
from market import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='market/index.html'), name='index'),

    url(r'^shops/$', views.shops, name='shops'),
    url(r'^shops/(?P<shop_id>\d+)/$', views.shops, name='shop'),
    url(r'^shops/(?P<shop_id>\d+)/(?P<good_id>\d+)/$', views.shops, name='shop_good'),

    url(r'^goods/$', views.goods, name='goods'),
    url(r'^goods/(?P<good_id>\d+)/$', views.goods, name='good'),

    url(r'^basket/$', views.basket_show, name='basket'),
    url(r'^basket/(?P<good_id>\d+)/add/$', views.basket_add, name='basket_add'),
    url(r'^basket/(?P<good_id>\d+)/remove/$', views.basket_remove, name='basket_remove'),

    url(r'^compare/$', views.compare, name='compare'),
    url(r'^compare/(?P<good_id>\d+)/add/$', views.compare_add, name='compare_add'),
    url(r'^compare/(?P<good_id>\d+)/remove/$', views.compare_remove, name='compare_remove'),

    url(r'^search/$', views.search, name='search'),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^pass_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^logout/$', views.logout_custom, name='logout'),
]