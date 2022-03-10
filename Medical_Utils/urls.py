"""Medical_Utils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from util.views import homePage
from util.views import login
from util.views import signup
from util.views import saveUser
from util.views import findDisease
from util.views import prevDiagnosis
from util.views import addNewDiagnosis
from util.views import saveNewDiagnosis
from util.views import detail

admin.site.site_header = "Automatic Health Tracking System Admin"
admin.site.site_title = "Automatic Health Tracking System Admin Portal"
admin.site.index_title = "Welcome to Automatic Health Tracking System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
    path('login', login),
    path('thanks/', login),
    path('signup/', signup),
    path('signup/saveUser', saveUser),
    #path('', include(('util.urls',util), namespace='util'))
    path('prevDiagnosis/', prevDiagnosis, name='prevDiagnosis'),
    path('addNewDiagnosis/', addNewDiagnosis, name='addNewDiagnosis'),
    path('findDisease/', findDisease, name='findDisease'),
    path('addNewDiagnosis/saveNewDiagnosis/', saveNewDiagnosis, name='saveNewDiagnosis'),
    path('detail', detail, name='detail'),
]
