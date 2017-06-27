from django.conf.urls import url
from . import views
from mpcontribs.utils import get_user_explorer_name

urlpatterns = [
    url(r'^$', views.index, name=get_user_explorer_name(__file__))
]
