from allauth.socialaccount.providers.oauth2_provider_provider.urls import default_urlpatterns
from .provider import VKProvider

urlpatterns = default_urlpatterns(VKProvider)
