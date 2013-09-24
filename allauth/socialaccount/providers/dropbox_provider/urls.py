from allauth.socialaccount.providers.h_provider_provider.urls import default_urlpatterns

from .provider import DropboxProvider

urlpatterns = default_urlpatterns(DropboxProvider)
