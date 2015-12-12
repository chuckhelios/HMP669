"""emergency_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from rest_framework_bulk.routes import BulkRouter

from emergency_app.views import IndexView
from PatientSearch.views import *
from authentication.views import AccountViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'residents', ResidentInfoViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'incidentReport', IncidentReportViewSet)

bulkRouter = BulkRouter()
bulkRouter.register(r'vitalsigns',VitalsignsViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
    url(r'api/',include(bulkRouter.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),	
	url(r'^api/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/auth/logout/$', LogoutView.as_view(), name='logout'),
    # url(r'^.*$', IndexView.as_view(), name='index'),
    url(r'^.*$', IndexView.as_view(), name='index'),

]

