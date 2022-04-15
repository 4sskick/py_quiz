from django.conf.urls import url

from . import views as appViews

urlpatterns = [
    url(r'^$', appViews.index),
    url(r'^questions/', appViews.quiz)
]
