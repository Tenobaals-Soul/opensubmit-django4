from django.urls import include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from opensubmit import admin
from opensubmit.views import frontend, backend, lti, api, demo
from opensubmit.forms import MailForm

app_name='opensubmit'

urlpatterns = [
    # Frontend Login
    re_path(r'^demo/(?P<role>.*)/$', demo.LoginView.as_view(), name='demo'),
    re_path(r'^$', frontend.IndexView.as_view(), name='index'),
    re_path(r'', include('social_django.urls', namespace='social')),
    # Frontend views
    re_path(r'^logout/$', frontend.LogoutView.as_view(), name='logout'),
    re_path(r'^settings/$', frontend.SettingsView.as_view(), name='settings'),
    re_path(r'^impress/$', frontend.ImpressView.as_view(), name='impress'),
    re_path(r'^privacy/$', frontend.PrivacyView.as_view(), name='privacy'),
    re_path(r'^courses/$', frontend.CoursesView.as_view(), name='courses'),
    re_path(r'^archive/$', frontend.ArchiveView.as_view(), name='archive'),
    re_path(r'^dashboard/$', frontend.DashboardView.as_view(), name='dashboard'),
    re_path(r'^details/(?P<pk>\d+)/$', frontend.SubmissionDetailsView.as_view(), name='details'),
    re_path(r'^machine/(?P<pk>\d+)/$', frontend.MachineDetailsView.as_view(), name='machine'),
    re_path(r'^assignments/(?P<pk>\d+)/lti/$', lti.DispatcherView.as_view(), name='lti'),
    re_path(r'^assignments/(?P<pk>\d+)/lti/submission/$', lti.SubmissionView.as_view(), name='lti_submission'),
    re_path(r'^assignments/(?P<pk>\d+)/new/$', frontend.SubmissionNewView.as_view(), name='new'),
    re_path(r'^assignments/(?P<pk>\d+)/validity_testscript/$', frontend.ValidityScriptView.as_view(), name='validity_script'),
    re_path(r'^assignments/(?P<pk>\d+)/full_testscript/$', frontend.FullScriptView.as_view(), name='full_testscript'),
    re_path(r'^assignments/(?P<pk>\d+)/description_file/$', frontend.DescriptionFileView.as_view(), name='assignment_description_file'),
    re_path(r'^withdraw/(?P<pk>\d+)/$', frontend.SubmissionWithdrawView.as_view(), name='withdraw'),
    re_path(r'^withdraw/(?P<pk>\d+)/lti/$', lti.WithdrawView.as_view(), name='lti_withdraw'),
    re_path(r'^update/(?P<pk>\d+)/$', frontend.SubmissionUpdateView.as_view(), name='update'),
    re_path(r'^submission/(?P<pk>\d+)/attachment_file/$', frontend.AttachmentFileView.as_view(), name='submission_attachment_file'),
    re_path(r'^submission/(?P<pk>\d+)/grading_file/$', frontend.GradingFileView.as_view(), name='submission_grading_file'),
    # Backend
    re_path(r'^teacher/', include((admin.teacher_backend.urls[0], app_name), namespace=admin.teacher_backend.urls[1])),
    re_path(r'^teacher/', include((admin.teacher_backend.urls[0], app_name), namespace=admin.teacher_backend.urls[2])),
    re_path(r'^grappelli/', include('grappelli.urls')),
    re_path(r'^preview/(?P<pk>\d+)/$', backend.PreviewView.as_view(), name='preview'),
    re_path(r'^assignments/(?P<pk>\d+)/duplicates/$', backend.DuplicatesView.as_view(), name='duplicates'),
    re_path(r'^assignments/(?P<pk>\d+)/archive/$', backend.AssignmentArchiveView.as_view(), name='assarchive'),
    re_path(r'^course/(?P<pk>\d+)/archive/$', backend.CourseArchiveView.as_view(), name='coursearchive'),
    re_path(r'^course/(?P<pk>\d+)/gradingtable/$', backend.GradingTableView.as_view(), name='gradingtable'),
    re_path(r'^mergeusers/(?P<primary_pk>\d+)/(?P<secondary_pk>\d+)/$', backend.MergeUsersView.as_view(), name='mergeusers'),
    re_path(r'^mail/receivers=(?P<user_list>.*)$', backend.MailFormPreview(MailForm), name='mailstudents'),
    re_path(r'^mail/course=(?P<course_id>\d+)$', backend.MailFormPreview(MailForm), name='mailcourse'),
    # Executor URLs
    re_path(r'^download/(?P<pk>\d+)/validity_testscript/secret=(?P<secret>\w+)$', api.ValidityScriptView.as_view(), name='validity_script_secret'),
    re_path(r'^download/(?P<pk>\d+)/full_testscript/secret=(?P<secret>\w+)$', api.FullScriptView.as_view(), name='full_testscript_secret'),
    re_path(r'^jobs/$', api.jobs, name='jobs'),
    re_path(r'^machines/$', api.MachinesView.as_view(), name='machines'),
    # Error pages
    re_path(r'^403/$', TemplateView.as_view(template_name='403.html')),
    re_path(r'^404/$', TemplateView.as_view(template_name='404.html')),
    re_path(r'^500/$', TemplateView.as_view(template_name='500.html')),
]

# only working when DEBUG==FALSE
# on production systems, static files are served directly by Apache
urlpatterns += staticfiles_urlpatterns()

