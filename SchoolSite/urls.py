"""SchoolSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.urls import include
import accounts.views as account_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', account_view.home_view, name='home'),
    url(r'', include('main_site_app.urls')),
    path('account/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admissions/', include('admission_app.urls')),
    # path('admissions/', account_view.admissions_view, name='admissions'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
