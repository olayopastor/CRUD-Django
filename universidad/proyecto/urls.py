from django.conf.urls import url
from . import views
from views import AlumnosListView, AlumnosDetailView, AlumnosCreateView, AlumnosDeleteView, AlumnosUpdateView, ProfesoresListView, ProfesoresDetailView, ProfesoresCreateView, ProfesoresDeleteView, ProfesoresUpdateView, MateriasUpdateView

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^mat_disp', views.mat_disp, name='mat_disp'),
    url(r'^mat_vista', views.mat_vista, name='mat_vista'),
    #url(r'^alu_vista2', MateriasListView.as_view(), name='alu_vista2'),
    url(r'^mat_asig/(?P<pk>[0-9]+)/$', MateriasUpdateView.as_view(), name='mat_asig'),

    url(r'^alu_vista', AlumnosListView.as_view(), name='alu_vista'),
    url(r'^(?P<pk>[0-9]+)/$', AlumnosDetailView.as_view(), name='alu_detail'),
    url(r'^alu_new', AlumnosCreateView.as_view(), name='alu_new'),
    url(r'^alu_delete/(?P<pk>[0-9]+)/$', AlumnosDeleteView.as_view(), name='alu_delete'),
    url(r'^alu_update/(?P<pk>[0-9]+)/$', AlumnosUpdateView.as_view(), name='alu_update'),


    url(r'^pro_vista', ProfesoresListView.as_view(), name='pro_vista'),
    url(r'^pro_detail/(?P<pk>[0-9]+)/$', ProfesoresDetailView.as_view(), name='pro_detail'),
    url(r'^pro_new', ProfesoresCreateView.as_view(), name='pro_new'),
    url(r'^pro_delete/(?P<pk>[0-9]+)/$', ProfesoresDeleteView.as_view(), name='pro_delete'),
    url(r'^pro_update/(?P<pk>[0-9]+)/$', ProfesoresUpdateView.as_view(), name='pro_update'),
    #url(r'^product(?P<pk>[0-9]+)/$', views.products_detail, name='product'),
    #url(r'^(?P<pk>[0-9]+)/$', views.products_detail, name='product'),
    #url(r'^new', views.new_product, name='new'),
    #url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_product, name='delete'),
]
