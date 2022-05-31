from django.conf.urls import url

from . import views as appViews

urlpatterns = [
    url(r'^$', appViews.index),
    url(r'^evaluasi/', appViews.serve_evaluation),
    url(r'^adminhsi/', appViews.serve_admin)
]
