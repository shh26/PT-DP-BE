"""
URL configuration for stcdp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/opportunity/',include('opportunity.opportunity_urls')),
    path('api/v1/project/',include('project.urls.project_urls')),
    path('api/v1/decision/',include('project.urls.decision_urls')),
    path('api/v1/risk/',include('project.urls.risk_urls')),
    path('api/v1/users/', include('users.urls')),
    path('auth/adfs/', include('django_auth_adfs.urls', namespace='django_auth_adfs')),
    path('api/v1/cost/',include('project.urls.cost_urls')),
    path('api/v1/feedback/', include('project.urls.feedback_urls')),
    path('api/v1/comment/',include('opportunity.comment_urls')),
]
