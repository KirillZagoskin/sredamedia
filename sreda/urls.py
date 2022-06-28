from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from users.views import username_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='sreda/home.html'), name='sreda_home'),
    path('<username>', username_view, name='username'),
# ] + staticfiles_urlpatterns()
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)