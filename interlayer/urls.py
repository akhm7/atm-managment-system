from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings

from typing import Pattern
from crudapp import views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django_filters.views import FilterView
admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("accounts/", include("django.contrib.auth.urls")),

    path('api/',include('myapi.urls')),
    #path('atms/', views.IndexView.as_view(), name='atms'),
    path('atms/', views.TestAtmView.as_view(), name='atms'),
    path('', views.IndexPage, name='index'),
    path('atms/statistic/', views.atmStatistic, name='static'),
    path('atms/<int:pk>/', views.AtmDetailView.as_view(), name='detail'),
    path('atms/edit/<int:pk>/', views.edit, name='edit'),
    path('atms/create/', views.create, name='create'),
    path('atms/delete/<int:pk>/', views.delete, name='delete'),
    path('atms/photo/upload/', views.image_upload_view, name='photo-upload'),
    path('atms/photo/upload/<int:pk>/', views.image_upload_view, name='photo-upload-num'),

    path('ticket/<int:pk>/', views.TicketView, name='ticket'),
    #path('ticket/<int:pk>/', views.TicketView.as_view(), name='ticket'),

    
    path('model/', views.ModelAtmView.as_view(), name='model-list'),
    path('model/create', views.modelCreate, name='model-create'),
    path('model/delete/<int:pk>/', views.modelDelete, name='model-delete'),
    path('model/edit/<int:pk>/', views.modelEdit, name='model-edit'),
    path('function/', views.FunctionModelAtmView.as_view(), name='function-list'),
    path('function/create', views.functionCreate, name='function-create'),
    path('function/delete/<int:pk>/', views.functionDelete, name='function-delete'),
    path('function/edit/<int:pk>/', views.functionEdit, name='function-edit'),
    path('tse/', views.ModelTseView.as_view(), name='tse-list'),
    path('tse/status/<int:pk>/', views.regtseStatusChange, name='regtse-status-change'),
    path('device/', views.ModelDeviceView.as_view(), name='device-list'),
    path('request/', views.ModelRequestView.as_view(), name='request-list'),
    path('request/<int:pk>/', views.requestShow, name='request-full'),
    path('device/status/<int:pk>/', views.regdevStatusChange, name='regdev-status-change'),
    path('profile/', views.profile, name='users-profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password-change'),

    path('servicedesk/', views.ModelTicketView.as_view(), name='servicedesk'),
    path('servicedesk/closed/', views.ModelTicketClosedView.as_view(), name='servicedesk-close'),
    path('servicedesk/atm/<int:id>/', views.ModelTicketAtmView.as_view(), name='servicedesk-atm'),
    path('servicedesk/users/', views.ModelTicketUsersView.as_view(), name='servicedesk-users'),
    path('pcipts/', views.ModelPCIPTSView.as_view(), name='pcipts'),
    path('test/tse/', views.ModelTseTestView.as_view(), name='tse-list-test'),
    path('test/tse/status/<int:pk>/', views.regtseTestStatusChange, name='regtse-status-change-test'),
    path('test/device/', views.ModelDeviceTestView.as_view(), name='device-list-test'),
    path('test/request/', views.ModelRequestTestView.as_view(), name='request-list-test'),
    path('test/request/<int:pk>/', views.requestTestShow, name='request-full-test'),
    path('test/device/status/<int:pk>/', views.regdevTestStatusChange, name='regdev-status-change-test'),
    path('export/csv/', views.export_report_csv, name='export_report_csv'),
    path('telegramapi/', views.telegramApi, name='telegramApi'),
    path('tg/users/<int:pk>/<int:mfo>/', views.tgUserChangeMfo, name='tg-user-change'),
    #path('search/', views.FilterView.as_view(filterset_class=AtmFilter, template_name='crudapp/atms-filter-list.html'), name='searcher'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
