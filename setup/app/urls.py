from django.conf.urls import url

from . import views as appViews

urlpatterns = [
    url(r'^$', appViews.index),
    url(r'^evaluasi/', appViews.quiz),
    url(r'^adminhsi/', appViews.admin)
]
