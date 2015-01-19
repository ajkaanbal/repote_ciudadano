from django.conf.urls import patterns, url
from .views import ReportList, Report

urlpatterns = patterns(
    '',
    url(
        regex=r'^reports/$',
        view=ReportList.as_view(),
        name='report-list'
    ),
    url(
        regex=r'^reports/(?P<pk>\d+)/$',
        view=Report.as_view(),
        name='report-detail'
    )
)
