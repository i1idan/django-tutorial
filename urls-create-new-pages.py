## create new app named pages

manage.py startapp pages


#####change views.py in  page as follows:



from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	return HttpResponse('<h1>Hello World</h1>')
     #return render(request, home.html, {})
     
def contact_view(request, *args, **kwargs):
	return HttpResponse('<h1>Contact page</h1>')

#####change urls.py in  page as follows:

"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from pages.views import home_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
]


