"""
URL configuration for basic_app project.

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
from django.urls import path
from myapp import views
from django.views.generic.base import RedirectView

urlpatterns = [ 
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('contact/', views.contact_us),
    path('about/', views.about_us),
    path('user-list/', views.user_list, name="user_list"),
    path('create-account/', views.create_account, name='create_account'),
    path('delete-account/<int:account_id>/', views.delete_bank_account, name = 'delete_bank_account'),
    path('edit-account/<int:account_id>/', views.edit_bank_account, name = 'edit_bank_account'),

    #Relative Path
    path("red_rel", RedirectView.as_view( url = "www.google.com")),
    path("relative", views.RelativePageView),

    #External Path
    path("red_ext", RedirectView.as_view( url = "http://google.com")),
    path("external", views.ExternalPageView)

]
