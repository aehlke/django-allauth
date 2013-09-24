from allauth.socialaccount.providers.h_provider_provider.urls import default_urlpatterns
from .provider import VimeoProvider

urlpatterns = default_urlpatterns(VimeoProvider)
