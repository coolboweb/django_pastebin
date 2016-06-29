from django.conf.urls import url
from . import views
from paste.views import PasteCreateView
urlpatterns = [
    url(r'^$', PasteCreateView.as_view(), name='main_add_page'),
    url(r'^main/$', views.main_view, name='main_page'),
]
