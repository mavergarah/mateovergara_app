"""mateovergara_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
# from django.conf.urls import url: esta fue removida a partir de Django 3.0
from . import views

from django.conf import settings

# Esto es para que en el título de pestaña salga este nombre
admin.site.site_title = 'Mateo Vergara'
# Esto es para que en la parte superior izquierda salga este nombre
admin.site.site_header = 'Mateo Vergara - Administrator'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', include('about.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('calculations/', include('calculations.urls')),
    path('admin/', admin.site.urls),
]

# Dado que, en el model los campos IMAGE generan una url para cada imagen
# se hace necesario incluir estas urls en este archivo. Esto para cuando
# DEBUG esté activo.
if settings.DEBUG:
    from django.urls import re_path
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
